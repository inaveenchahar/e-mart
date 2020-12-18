from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('<cp_id>/increase-quantity/', views.increase_quantity, name='increase_quantity'),
    path('<cp_id>/decrease-quantity/', views.decrease_quantity, name='decrease_quantity'),
    path('<cp_id>/remove-cart-product/', views.remove_cart_product, name='remove_cart_product'),
    path('<c_slug>/<p_slug>/<id>/added-to-cart/', views.cart_product, name='cart_product'),
]
