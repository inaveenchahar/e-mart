from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('manage-address/', views.manage_addresses, name='manage_addresses'),
    path('manage-address/<id>/delete-address/', views.delete_address, name='delete_address'),
    path('manage-address/<id>/update-address/', views.update_address, name='update_address'),
    path('manage-address/<id>/default-address/', views.select_default_address, name='default_address'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
]