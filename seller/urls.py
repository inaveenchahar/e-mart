from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('all-orders/', views.all_orders, name='all_orders'),
    path('yet-to-be-shipped-orders/', views.yet_shipped_orders, name='yet_shipped'),
    path('shipped-orders/', views.shipped_orders, name='shipped_orders'),
    path('delivered-orders/', views.delivered_orders, name='delivered_orders'),
    path('all-orders/<cart_id>/', views.order_details, name='order_details'),
    path('all-orders/<cart_id>/marked-shipped/', views.marked_shipped, name='marked_shipped'),
    path('all-orders/<cart_id>/marked-delivered/', views.marked_delivered, name='marked_delivered'),
]
