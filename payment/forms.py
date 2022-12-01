from django import forms

from payment.models import Fee


class SetFeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
