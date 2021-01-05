from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Order, Payment
from cart.models import Cart, CartProduct
from accounts.models import UserAddress
from accounts.forms import UserAddressForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay
import datetime
from django.core.mail import send_mail


# Create your views here.


def order_history(request):
    if request.user.is_authenticated:
        all_completed_carts = Cart.objects.filter(user=request.user, completed=True)
        # all_cart_products = all_completed_carts.cartproduct_set.all()
        # print(all_cart_products)
        all_orders = Order.objects.filter(order_by=request.user, completed=True).order_by('-added_on')
        return render(request, 'order_history.html', {'all_orders': all_orders, 'all_completed_carts': all_completed_carts})
    else:
        return redirect('main:homepage')


def order_create(request, id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=id, user=request.user)
        order_amount = int(cart.cart_value) * 100
        if cart.delivery_charges > 0:
            order_amount = order_amount + (settings.DELIVERY_CHARGE * 100)
        order_currency = 'INR'
        order_receipt = 'order_receipt_' + str(request.user.username)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        resposne = client.order.create({'amount':order_amount, 'currency':order_currency, 'receipt':order_receipt, 'notes':{}})
        order_id = resposne['id']
        new_order = Order.objects.create(
            cart=cart,
            order_by=request.user,
            order_id=order_id,
            order_amount=order_amount,
        )
        return redirect('payment:order_payment', cart.id, new_order.order_id)
    return redirect('main:homepage')


def order_payment(request, cart_id, order_id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        order = get_object_or_404(Order, order_id=order_id)
        cart_products = CartProduct.objects.filter(cart=cart)
        ud_address = UserAddress.objects.filter(user=request.user, default_address=True).last()
        if request.method == "POST":
            address_form = UserAddressForm(request.POST)
            if address_form.is_valid():
                for adres in UserAddress.objects.filter(user=request.user):
                    adres.default_address = False
                    adres.save()
                instance = address_form.save(commit=False)
                instance.default_address = True
                instance.user = request.user
                instance.save()
                return redirect('payment:order_payment', cart.id, order.order_id)
        else:
            address_form = UserAddressForm()
        total_address = UserAddress.objects.filter(user=request.user).order_by('-default_address')
        if total_address.count() >= 4:
            address_form = None
        return render(request, 'order_payment.html', {'cart': cart,
                                                   'cart_products': cart_products,
                                                   'ud_address': ud_address,
                                                   'address_form': address_form,
                                                   'total_address': total_address,
                                                   'order': order,
                                                   'auth_key': settings.RAZORPAY_KEY_ID,
                                                   })
    else:
        return redirect('main:homepage')


def payment_default_address(request, cart_id, order_id, id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        order = get_object_or_404(Order, order_id=order_id)
        for adres in UserAddress.objects.filter(user=request.user):
            adres.default_address = False
            adres.save()
        address = get_object_or_404(UserAddress, id=id)
        address.default_address = True
        address.save()
        return redirect('payment:order_payment', cart.id, order.order_id)


@csrf_exempt
def transaction_view(request, cart_id, order_id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        order = get_object_or_404(Order, order_id=order_id)
        if request.method == 'POST':
            payment_id = request.POST.get("razorpay_payment_id", "")
            signature = request.POST.get("razorpay_signature", "")
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            try:
                params_dict = {
                    'razorpay_order_id': order.order_id,
                    'razorpay_payment_id': payment_id,
                    'razorpay_signature': signature,
                }
                '''
                Creating objects in Payment Model
                '''
                client.utility.verify_payment_signature(params_dict)
                order.completed = True
                order.address = UserAddress.objects.filter(user=request.user, default_address=True).last()
                order.save()
                cart.completed = True
                cart.ordered_on = datetime.datetime.now()
                cart.save()
                cart_products = CartProduct.objects.filter(cart=cart)
                payment = Payment.objects.create(
                    order=order,
                    transaction_id=payment_id,
                    currency='INR',
                    signature=signature,
                    paid_by=request.user,
                    status='CAPTURED'
                )
                try:
                    send_mail(
                        subject="Purchase Successful",
                        recipient_list=[request.user.email],
                        from_email=settings.EMAIL_HOST_USER,
                        fail_silently=True,
                        message="Your purchase has been done successfully and delivery will be done within"
                                " 6-7 business days\n"
                                "Thankyou😊 for shopping with us"
                    )
                    print('email sent')
                except Exception as e:
                    print(e)
                payment.save()
                messages.success(request, 'order successfully placed')
                return redirect('main:homepage')
            except Exception as e:
                messages.error(request, 'We are facing some issue kindly try again after some time')
                return redirect('cart:view_cart')
    else:
        return redirect('main:homepage')
