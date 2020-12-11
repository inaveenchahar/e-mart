from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Cart, CartProduct
from accounts.models import UserAddress
from accounts.forms import UserAddressForm
from products.models import Category, Product
from django.contrib import messages

from payments.models import Order, Payment
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings
# Create your views here.


def cart_product(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    p_quantity = 1
    if request.method == 'POST':
        p_quantity = request.POST.get('p_quantity')
        if int(p_quantity) < 1:
            p_quantity = 1
    if request.user.is_authenticated:
        if Cart.objects.filter(completed=False, user=request.user):
            cart = Cart.objects.get(completed=False, user=request.user)
        else:
            cart = Cart.objects.create(user=request.user)
        if CartProduct.objects.filter(cart=cart, product=product):
            c_product = CartProduct.objects.get(cart=cart, product=product)
        else:
            c_product = CartProduct.objects.create(
                cart=cart,
                product=product,
                price=product.price,
                quantity=0
            )
        c_product.quantity += int(p_quantity)
        c_product.save()
        messages.success(request, "You have successfully added {prdt} in your cart.".format(prdt=product))
        return redirect('main:homepage')
    return render(request, 'product_details.html', {'category': category, 'product': product})


def update_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(completed=False, user=request.user)
        if request.method == 'POST':
            try:
                product = cart.cartproduct_set.get(pk=request.POST['product'])
                p_quantity = int(request.POST['p_quantity'])
                if p_quantity < 1:
                    prod = CartProduct.objects.get(id=product.id)
                    prod.delete()
                    return redirect('cart:view_cart')
            except (KeyError, CartProduct.DoesNotExist):
                return HttpResponse("error occurred")
            else:
                product.quantity = p_quantity
                product.save()
                return redirect('cart:view_cart')
    else:
        return HttpResponse("Login to update your cart")


def view_cart(request):
    if request.user.is_authenticated:
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()

        if tcp > 0:
            cart = Cart.objects.filter(completed=False, user=request.user).last()
            cart_products = CartProduct.objects.filter(cart=cart)
            total = 0
            for item in cart_products:
                total = total + (item.quantity * item.product.price)
            cart.cart_value = total
            cart.save()
            return render(request, 'view_cart.html',{'cart': cart, 'cart_products': cart_products, 'tcp': tcp, 'total': total})
        else:
            empty_cart_message = 'Your cart is empty. Add products to it.'
            return render(request, 'view_cart.html', {'empty_cart_message': empty_cart_message, 'tcp': tcp})
    else:
        tcp = 0
        return render(request, 'view_cart.html', {'tcp': tcp})








# def view_cart(request):
#     if request.user.is_authenticated:
#         tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False, product__visible=True).count()
#
#         if tcp > 0:
#             cart = Cart.objects.filter(completed=False, user=request.user).last()
#             cart_products = CartProduct.objects.filter(cart=cart)
#             total = 0
#             for item in cart_products:
#                 total = total + (item.quantity * item.product.price)
#             cart.cart_value = total
#             cart.save()
#             ud_address = UserAddress.objects.filter(user=request.user, default_address=True).last()
#
#             address_form = UserAddressForm(request.POST or None)
#             total_address = UserAddress.objects.filter(user=request.user).count()
#             if total_address >= 6:
#                 address_form = None
#             return render(request, 'view_cart.html', {'cart': cart, 'cart_products': cart_products, 'tcp': tcp, 'total': total, 'ud_address': ud_address, 'address_form': address_form, 'total_address': total_address})
#         else:
#             empty_cart_message = 'Your cart is empty. Add products to it.'
#             return render(request, 'view_cart.html', {'empty_cart_message': empty_cart_message, 'tcp': tcp})
#     else:
#         tcp = 0
#         return render(request, 'view_cart.html', {'tcp': tcp})
