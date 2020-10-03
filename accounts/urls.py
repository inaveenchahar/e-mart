from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
]