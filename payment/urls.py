from django.urls import path

from payment.views import payment_page

urlpatterns = (
    path('', payment_page, name='payment'),
)