from django.urls import path

from payment.views import payment_page, SetPaymentView

urlpatterns = (
    path('', payment_page, name='payment'),
    path('set-payment/', SetPaymentView.as_view(), name='set payment'),
)