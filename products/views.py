from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from cart.models import CartProduct

# Create your views here.


def category_index(request):
    all_categories = Category.objects.filter(visible=True).order_by('order')
    tcp = 0
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    return render(request, 'category_index.html', {'all_categories': all_categories, 'tcp': tcp})


def category_details(request, c_slug):
    category = get_object_or_404(Category, slug=c_slug)
    all_products = Product.objects.filter(category=category).order_by('order')
    tcp = 0
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    return render(request, 'category_details.html', {'category': category, 'all_products': all_products, 'tcp': tcp})


def product_details(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    tcp = 0
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    return render(request, 'product_details.html', {'category': category, 'product': product, 'tcp': tcp})
