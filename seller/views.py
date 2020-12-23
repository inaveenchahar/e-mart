from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from cart.models import Cart

# Create your views here.


def dashboard(request):
    if request.user.is_superuser:
        all_users = User.objects.filter(is_superuser=False).count()
        all_orders = Cart.objects.filter(completed=True).count()
        ordered_items = Cart.objects.filter(completed=True, delivered=False)
        delivered_items = Cart.objects.filter(completed=True, delivered=True)
        return render(request, 'dashboard.html', {'all_users': all_users, 'all_orders': all_orders, 'ordered_items': ordered_items, 'delivered_items': delivered_items})
    else:
        return redirect('main:homepage')


def index_seller(request):
    if request.user.is_superuser:
        ordered_items = Cart.objects.filter(completed=True, delivered=False).order_by('-ordered_on')
        delivered_items = Cart.objects.filter(completed=True, delivered=True).order_by('-delivered_on')
        return render(request, 'index_seller.html', {'ordered_items': ordered_items, 'delivered_items': delivered_items})
    else:
        return redirect('main:homepage')

