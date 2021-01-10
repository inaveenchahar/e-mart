from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.models import CartProduct


def category_details(request, c_slug):
    """
        displays all the products of a specific category
    """
    category = get_object_or_404(Category, slug=c_slug)
    all_products = Product.objects.filter(category=category, visible=True).order_by('order')
    tcp = 0
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    return render(request, 'category_details.html', {'category': category, 'all_products': all_products, 'tcp': tcp})


def product_details(request, p_slug, id):
    """
        displays the details of selected product
    """
    product = get_object_or_404(Product, slug=p_slug, id=id)
    tcp = 0
    already_exists = False
    if request.user.is_authenticated:
        """
            tcp = total cart products
            checks if currently selected product is already in cart or not
        """
        cart_product = CartProduct.objects.filter(cart__user=request.user, cart__completed=False)
        for p in cart_product:
            if p.product == product:
                already_exists = True

        tcp = cart_product.count()
    return render(request, 'product_details.html', {'product': product, 'tcp': tcp, 'already_exists': already_exists})
