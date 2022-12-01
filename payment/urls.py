from django.urls import path

from payment.views import SetPaymentView, pay_page

urlpatterns = (
    path('', pay_page, name='payment'),
    path('set-payment/', SetPaymentView.as_view(), name='set payment'),
)