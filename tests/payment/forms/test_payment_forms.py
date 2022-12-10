from django.test import TestCase

from payment.forms import PaymentForm


class PaymentFormTests(TestCase):
    def test_profile_form_valid_data(self):
        valid_payment_data = {
            'card_number': '1234123412341234',
            'card_cvv': '100',
            'card_expiry_date': '2024-01-01'

        }
        form = PaymentForm(valid_payment_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_data_expiry_date_passed(self):
        valid_payment_data = {
            'card_number': '1234123412341234',
            'card_cvv': '100',
            'card_expiry_date': '2000-01-01'

        }
        form = PaymentForm(valid_payment_data)
        self.assertFalse(form.is_valid())