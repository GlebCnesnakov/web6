from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.messages.views import SuccessMessageMixin



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация по email'}

    def get_success_url(self):
        return self.get_redirect_url() or reverse_lazy('menu')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('users:login'))


User = get_user_model()

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {'title': 'Регистрация'}

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    fields = ['first_name', 'last_name', 'email']  # можно расширить
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile')


class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:profile')
    success_message = "Пароль успешно изменён!"
