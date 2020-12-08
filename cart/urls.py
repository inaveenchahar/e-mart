from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart-items/', views.view_cart, name='view_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('<c_slug>/<p_slug>/<id>/added-to-cart/', views.cart_product, name='cart_product'),
]

