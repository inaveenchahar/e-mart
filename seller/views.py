from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from django.db.models import Sum
import datetime


#   only superuser can access these views

def dashboard(request):
    """
        displays all orders related information aka dashboard
    """
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


def all_orders(request):
    """
        displays all order , shipped, delivered together at one place
    """
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
    """
        displays all shipped orders
    """
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True, shipped=True, delivered=False)
        return render(request, 'shipped_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')


def delivered_orders(request):
    """
        displays all delivered orders
    """
    if request.user.is_superuser:
        all_orders = Cart.objects.filter(completed=True, shipped=True, delivered=True)
        return render(request, 'delivered_orders.html', {'all_orders': all_orders})
    else:
        return redirect('main:homepage')


def order_details(request, cart_id):
    """
        displays all details of selected order
    """
    if request.user.is_superuser:
        order = get_object_or_404(Cart, id=cart_id)
        return render(request, 'order_details.html', {'order': order})
    else:
        return redirect('main:homepage')


def marked_shipped(request, cart_id):
    """
        marked selected order as shipped
    """
    if request.user.is_superuser:
        cart = get_object_or_404(Cart, id=cart_id)
        cart.shipped = True
        cart.shipped_on = datetime.date.today()
        cart.save()
        return redirect('seller:order_details', cart.id)
    else:
        return redirect('main:homepage')


def marked_delivered(request, cart_id):
    """
        marked selected order as delivered
    """
    if request.user.is_superuser:
        cart = get_object_or_404(Cart, id=cart_id)
        if cart.shipped is True:
            cart.delivered = True
            cart.delivered_on = datetime.date.today()
            cart.save()
        return redirect('seller:order_details', cart.id)
    else:
        return redirect('main:homepage')
