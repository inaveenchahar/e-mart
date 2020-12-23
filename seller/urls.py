from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order-status/', views.index_seller, name='index_seller'),
]
