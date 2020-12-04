from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from cart.models import CartProduct

# Create your views here.


def product_details(request, c_slug, p_slug, id):
    category = get_object_or_404(Category, slug=c_slug)
    product = get_object_or_404(Product, slug=p_slug, id=id)
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    else:
        tcp = 0
    return render(request, 'product_details.html', {'category': category, 'product': product, 'tcp': tcp})
