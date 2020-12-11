from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Order, Payment
from cart.models import Cart, CartProduct
from accounts.models import UserAddress
from accounts.forms import UserAddressForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay

# Create your views here.


def order_create(request, id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=id, user=request.user)
        order_amount = int(cart.cart_value) * 100
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
        return redirect('payment:order_view', cart.id, new_order.id)
    return redirect('main:homepage')


def order_view(request, cart_id, order_id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, id=cart_id, user=request.user)
        order = get_object_or_404(Order, id=order_id)
        cart_products = CartProduct.objects.filter(cart=cart)
        ud_address = UserAddress.objects.filter(user=request.user, default_address=True).last()
        address_form = UserAddressForm(request.POST or None)
        total_address = UserAddress.objects.filter(user=request.user).count()
        if total_address >= 6:
            address_form = None
        return render(request, 'order_view.html', {'cart': cart,
                                                   'cart_products': cart_products,
                                                   'ud_address': ud_address,
                                                   'address_form': address_form,
                                                   'total_address': total_address,
                                                   'order': order,
                                                   'auth_key': settings.RAZORPAY_KEY_ID,
                                                   })
    else:
        return redirect('main:homepage')

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
                order.save()
                cart.completed = True
                cart.save()
                payment = Payment.objects.create(
                    order=order,
                    transaction_id=payment_id,
                    currency='INR',
                    signature=signature,
                    paid_by=request.user,
                    status='CAPTURED'
                )
                payment.save()
                messages.success(request, 'order successfully placed')
                return redirect('main:homepage')
            except Exception as e:
                return HttpResponse('Payment Signature Mismatch')
    else:
        return redirect('main:homepage')
