from django.shortcuts import render, redirect
from cart.models import Cart

# Create your views here.


def index_seller(request):
    if request.user.is_superuser:
        ordered_items = Cart.objects.filter(completed=True, delivered=False).order_by('-ordered_on')
        delivered_items = Cart.objects.filter(completed=True, delivered=True).order_by('-delivered_on')
        return render(request, 'index_seller.html', {'ordered_items': ordered_items, 'delivered_items': delivered_items})
    else:
        return redirect('main:homepage')

