from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # path('', views.category_index, name='category_index'),
    path('<c_slug>/', views.category_details, name='category_details'),
    path('<p_slug>/<id>/', views.product_details, name='product_details'),
]
