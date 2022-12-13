from django.test import TestCase

from accounts.forms import UserCreateForm


class SignUpProfileFormTest(TestCase):
    def test_profile_form_valid_data_valid_building_code(self):
        valid_user_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'building_code': '1166',
            'email': 'testuser@mail.com',
            'password1': 'thisisapassword12',
            'password2': 'thisisapassword12',
        }
        form = UserCreateForm(valid_user_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_data_passwords_invalid_code_length(self):
        valid_user_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'building_code': '116',
            'email': 'testuser@mail.com',
            'password1': 'thisisapassword12',
            'password2': 'thisisapassword13',
        }
        form = UserCreateForm(valid_user_data)
        self.assertFalse(form.is_valid())

