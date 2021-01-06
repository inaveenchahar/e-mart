from django.shortcuts import render, redirect
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


def product_search(request):
    all_products = Product.objects.filter(visible=True)
    query = request.GET.get('q')
    print(query)
    if query:
        all_products = Product.objects.filter(visible=True, title__icontains=query).order_by('order')
        # for product in all_products:
        #     for category in product.category.all()[1]:
        #         print(category)
        return render(request, 'category_details.html', {'all_products': all_products})
    else:
        return redirect('main:homepage')

