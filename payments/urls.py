from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('order-create/<id>/', views.order_create, name='order_create'),
    path('view-order/<cart_id>/<order_id>/', views.order_view, name='order_view'),
    path('view-order/<cart_id>/<order_id>/transaction/', views.transaction_view, name='transaction_view'),
]
