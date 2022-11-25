from django.shortcuts import render


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


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