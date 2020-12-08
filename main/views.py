from django.shortcuts import render
from products.models import Category, Product
from cart.models import CartProduct
# Create your views here.


def homepage(request):
    all_categories = Category.objects.filter(visible=True).order_by('order')
    # all_products = Product.objects.filter(category__visible=True, order__lte=4).order_by('order')
    if request.user.is_authenticated:
        """
            tcp = total cart products
        """
        tcp = CartProduct.objects.filter(cart__user=request.user, cart__completed=False).count()
    else:
        tcp = 0
    return render(request, 'homepage.html', {'all_categories': all_categories, 'tcp': tcp})

