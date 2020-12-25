from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from cart.models import Cart
from django.db.models import Sum

# Create your views here.


def dashboard(request):
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True)
        yet_shipped_orders = Cart.objects.filter(completed=True, shipped=False, delivered=False)
        shipped_orders = Cart.objects.filter(completed=True, shipped=True, delivered=False)
        delivered_orders = Cart.objects.filter(completed=True, shipped=True, delivered=True)
        revenue_generated = Cart.objects.filter(completed=True).aggregate(Sum('cart_value'))['cart_value__sum']
        return render(request, 'dashboard.html', {'all_orders': all_orders,
                                                  'delivered_orders': delivered_orders,
                                                  'yet_shipped_orders': yet_shipped_orders,
                                                  'revenue_generated': revenue_generated,
                                                  'shipped_orders': shipped_orders
                                                  })
    else:
        return redirect('main:homepage')


def index_seller(request):
    if request.user.is_superuser:
        ordered_items = Cart.objects.filter(completed=True, delivered=False).order_by('-ordered_on')
        delivered_items = Cart.objects.filter(completed=True, delivered=True).order_by('-delivered_on')
        return render(request, 'index_seller.html', {'ordered_items': ordered_items, 'delivered_items': delivered_items})
    else:
        return redirect('main:homepage')


def all_orders(request):
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True)
        return render(request, 'all_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')


def yet_shipped_orders(request):
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True, shipped=False, delivered=False)
        return render(request, 'yet_shipped_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')


def shipped_orders(request):
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True, shipped=True, delivered=False)
        return render(request, 'shipped_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')


def delivered_orders(request):
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True, shipped=True, delivered=True)
        return render(request, 'delivered_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')



