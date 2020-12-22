from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('order-status/', views.index_seller, name='index_seller'),
]
