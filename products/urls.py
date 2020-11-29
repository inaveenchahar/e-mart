from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<c_slug>/<p_slug>/<id>/', views.product_details, name='product_details'),
    path('<c_slug>/<p_slug>/<id>/added-to-cart/', views.cart_product, name='cart_product'),
]
