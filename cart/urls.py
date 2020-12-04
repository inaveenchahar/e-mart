from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<c_slug>/<p_slug>/<id>/added-to-cart/', views.cart_product, name='cart_product'),
]

