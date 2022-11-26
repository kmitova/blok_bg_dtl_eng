from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from accounts.forms import UserCreateForm, UserLoginForm

UserModel = get_user_model()
# def register(request):
#     return render(request, 'accounts/register.html')


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('home page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('landing page')

# def login(request):
#     return render(request, 'accounts/login.html')


def register_admin(request):
    return render(request, 'accounts/register-admin.html')


def login_admin(request):
    return render(request, 'accounts/login-admin.html')


def profile_page(request):
    return render(request, 'accounts/profile-page.html')


def edit_profile_page(request):
    return render(request, 'accounts/edit-profile.html')


def delete_profile_page(request):
    return render(request, 'accounts/verify-page.html')