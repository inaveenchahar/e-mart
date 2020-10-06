from django.shortcuts import render
from products.models import Category, Product
# Create your views here.


def homepage(request):
    all_categories = Category.objects.filter(visible=True)
    all_products = Product.objects.filter(visible=True)
    return render(request, 'homepage.html', {'all_categories': all_categories, 'all_products': all_products})

