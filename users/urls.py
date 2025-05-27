from django.urls import path, register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "users"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name = "users/password_reset_form.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
    path('password-reset/', auth_views.PasswordResetView.as_view( template_name="users/password_reset_form.html", email_template_name="users/password_reset_email.html", success_url=reverse_lazy("users:password_reset_done")), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name="users/password_reset_confirm.html", success_url=reverse_lazy("users:password_reset_complete")), name='password_reset_confirm'),
]