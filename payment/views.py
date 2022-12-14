import datetime

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic as views


from payment.forms import SetFeeForm, PaymentForm
from payment.models import Fee

UserModel = get_user_model()


class SetPaymentView(views.CreateView):
    model = UserModel
    form_class = SetFeeForm
    template_name = 'payment/set-payment.html'
    success_url = reverse_lazy('home page')


def pay_page(request):
    if request.method == "GET":
        form = PaymentForm()
    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            name = payment.user.username
            email = payment.user.email
            paid_fee = Fee.objects.last().fee
            current_datetime = datetime.datetime.now()
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            current_date = datetime.date.today()
            html = render_to_string('payment/email.html', {
                'name': name,
                'email': email,
                'paid_fee': paid_fee,
                'current_time': current_time,
                'current_date': current_date

            })

            send_mail('Mail subject', 'Message content', 'noreply@blokbg.com', [payment.user.email],
                      html_message=html)
            return redirect('home page')

    last_fee = Fee.objects.last()

    context = {
        'form': form,
        'fee_amount': last_fee.fee,
        'fee_deadline': last_fee.deadline
    }

    return render(request, 'payment/payment-page.html', context)

