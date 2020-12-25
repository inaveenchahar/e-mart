from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('manage-address/', views.manage_addresses, name='manage_addresses'),
    path('manage-address/<id>/delete-address/', views.delete_address, name='delete_address'),
    path('manage-address/<id>/update-address/', views.update_address, name='update_address'),
    path('manage-address/<id>/default-address/', views.select_default_address, name='default_address'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),

    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

