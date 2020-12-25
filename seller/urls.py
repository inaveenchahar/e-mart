from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('yet-to-be-shipped-orders/', views.yet_shipped_orders, name='yet_shipped'),
    path('shipped-orders/', views.shipped_orders, name='shipped_orders'),
    path('delivered-orders/', views.delivered_orders, name='delivered_orders'),
    path('order-status/', views.index_seller, name='index_seller'),
]
