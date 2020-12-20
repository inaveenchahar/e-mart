from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.order_history, name='order_history'),
    path('order-create/<id>/', views.order_create, name='order_create'),
    path('view-order/<cart_id>/<order_id>/', views.order_payment, name='order_payment'),
    path('view-order/<cart_id>/<order_id>/transaction/', views.transaction_view, name='transaction_view'),
    path('view-order/<cart_id>/<order_id>/<id>/default-address/', views.payment_default_address, name='payment_default_address'),
]
