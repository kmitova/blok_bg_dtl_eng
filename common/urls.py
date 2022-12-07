from django.urls import path

from common.views import landing_page, about_page, t_and_c_page, privacy_page

urlpatterns = (
    path('', landing_page, name='landing page'),
    path('about/', about_page, name='about page'),
    path('terms&conditions/', t_and_c_page, name='t-and-c page'),
    path('privacy-and-data-protection/', privacy_page, name='privacy page'),
)