from django.core.exceptions import ValidationError
from django.test import TestCase


from accounts.models import AppUser


class AppUserModelTests(TestCase):
    # VALID_USER_DATA = {
    #     'first_name': 'Test',
    #     'last_name': 'User',
    #     'username': 'testuser',
    #     'building_code': '1166',
    #     'email': 'testuser@mail.com',
    #     'password1': 'thisisapassword12',
    #     'password2': 'thisisapassword12',
    # }

    def test_profile_create_valid_data(self):
        u = AppUser(
            first_name='Test',
            last_name='User',
            username='testuser',
            building_code=1166,
            email='testuser@mail.com',
            password='thisisapassword12',
            # password2='thisisapassword12',
        )
        u.full_clean()
        u.save()
        self.assertIsNotNone(u)

    def test_profile_create_invalid_building_code(self):
        u = AppUser(
            first_name='Test',
            last_name='User',
            username='testuser',
            building_code=0000,
            email='testuser@mail.com',
            password='thisisapassword12',
            # password2='thisisapassword12',
        )
        try:
            u.full_clean()
            u.save()
            self.fail()
        except ValidationError as e:
            self.assertIsNotNone(e)

    def test_profile_admin_create_valid_data(self):
        u = AppUser(
            first_name='Test',
            last_name='User',
            username='testuser',
            building_code=1166,
            email='testuser@mail.com',
            password='thisisapassword12',
            is_admin=True,
            admin_code=1234
            # password2='thisisapassword12',
        )
        u.full_clean()
        u.save()
        self.assertIsNotNone(u)

    def test_profile_admin_create_invalid_data_admin_code_invalid_length(self):
        u = AppUser(
            first_name='Test',
            last_name='User',
            username='testuser',
            building_code=1166,
            email='testuser@mail.com',
            password='thisisapassword12',
            is_admin=True,
            admin_code=123467
        )
        try:
            u.full_clean()
            u.save()
            self.fail()
        except ValidationError as e:
            self.assertIsNotNone(e)