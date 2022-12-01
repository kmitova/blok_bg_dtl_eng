from django import forms

from payment.models import Fee, Payment


class SetFeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("card_number", "card_cvv", "card_expiry_date")
