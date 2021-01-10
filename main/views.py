from django.shortcuts import render, redirect
from products.models import Category, Product
from cart.models import CartProduct


def homepage(request):
    """
        homepage view of the website
    """
    all_categories = Category.objects.filter(visible=True).order_by('order')
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    else:
        tcp = 0
    return render(request, 'homepage.html', {'all_categories': all_categories, 'tcp': tcp})


def product_search(request):
    """
        gets the search keyword from the navbar form and matches with the products name
    """
    query = request.GET.get('q')
    if query:
        all_products = Product.objects.filter(visible=True, title__icontains=query).order_by('order')
        return render(request, 'category_details.html', {'all_products': all_products})
    else:
        return redirect('main:homepage')

