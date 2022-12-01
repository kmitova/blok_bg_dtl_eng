from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from payment.forms import SetFeeForm

UserModel = get_user_model()


class SetPaymentView(views.CreateView):
    model = UserModel
    form_class = SetFeeForm
    template_name = 'payment/set-payment.html'
    success_url = reverse_lazy('home page')

def payment_page(request):
    return render(request, 'payment/payment-page.html',)
