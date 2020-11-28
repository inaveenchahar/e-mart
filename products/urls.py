from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<c_slug>/<p_slug>/<id>/', views.product_details, name='product_details')
]
