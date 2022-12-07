from django.shortcuts import render


def landing_page(request):
    return render(request, 'common/landing-page.html')


def about_page(request):
    return render(request, 'common/about.html')


def t_and_c_page(request):
    return render(request, 'common/t-and-c.html')

def privacy_page(request):
    return render(request, 'common/privacy.html')