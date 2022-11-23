from django.shortcuts import render


def landing_page(request):
    context = {}
    return render(request, 'common/landing-page.html', context)
