from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartProduct
from products.models import Category, Product
from django.contrib import messages
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
            )
        messages.success(request, "You have successfully added {prdt} in your cart.".format(prdt=product))
        return redirect('main:homepage')
    return render(request, 'product_details.html', {'category': category, 'product': product})