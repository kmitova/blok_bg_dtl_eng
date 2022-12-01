from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
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
            return redirect('home page')
    last_fee = Fee.objects.last()
    context = {
        'form': form,
        'fee_amount': last_fee.fee,
        'fee_deadline': last_fee.deadline
    }
    return render(request, 'payment/payment-page.html', context)




    # if request.method == "GET":
    #     form = PetCreateForm()
    #
    # else: # request is post
    #     form = PetCreateForm(request.POST)
    #     if form.is_valid():
    #         pet = form.save(commit=False)
    #         pet.user = request.user
    #         pet.save()
    #         return redirect('details user', pk=request.user.pk)
    #
    # context = {
    #     'form': form
    # }
    #
    # return render(request, 'pets/pet-add-page.html', context)

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)
    # return render(request, 'payment/payment-page.html',)
