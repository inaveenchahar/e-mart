from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Cart, CartProduct
from products.models import Category, Product
from django.contrib import messages
from django.db.models import Count
# Create your views here.


def cart_product(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    if request.user.is_authenticated:
        if Cart.objects.filter(completed=False, user=request.user):
            cart = Cart.objects.get(completed=False, user=request.user)
        else:
            cart = Cart.objects.create(user=request.user)
        if CartProduct.objects.filter(cart=cart, product=product):
            c_product = CartProduct.objects.get(cart=cart, product=product)
            c_product.quantity += 1
            c_product.save()
        else:
            new_cart_product = CartProduct.objects.create(
                cart=cart,
                product=product,
                price=product.price
            )
        messages.success(request, "You have successfully added {prdt} in your cart.".format(prdt=product))
        return redirect('main:homepage')
    return render(request, 'product_details.html', {'category': category, 'product': product})


def view_cart(request):
    if request.user.is_authenticated:
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
        if tcp > 0:
            cart = Cart.objects.filter(completed=False, user=request.user).last()
            cart_products = CartProduct.objects.filter(cart=cart)
            total = 0
            for item in cart_products:
                total = total + (item.quantity * item.product.price)
            cart.cart_value = total
            cart.save()
            return render(request, 'view_cart.html', {'cart': cart, 'cart_products': cart_products, 'tcp': tcp, 'total': total})
        else:
            empty_cart_message = 'Your cart is empty. Add products to it.'
            return render(request, 'view_cart.html', {'empty_cart_message': empty_cart_message, 'tcp': tcp})
    else:
        tcp = 0
        return render(request, 'view_cart.html', {'tcp': tcp})
