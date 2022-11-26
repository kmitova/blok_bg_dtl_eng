from django.shortcuts import render


def home_page(request):
    return render(request, 'dashboard.html')


def notifications_page(request):
    return render(request, 'notifications.html')
