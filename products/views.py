from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Cart

# Create your views here.


def product_details(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    return render(request, 'product_details.html', {'category': category, 'product': product})


def cart_product(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    new_cart = Cart.objects.create(product=product, user=request.user)
    return render(request, 'product_details.html', {'category': category, 'product': product})

"""
user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    product = models.ManyToManyField(Product)
"""


