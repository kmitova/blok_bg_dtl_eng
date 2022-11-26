from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'building_code', 'password1', 'password2')
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={'placeholder': 'First Name'}
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={'placeholder': 'Last Name'}
        #     ),
        #     'username': forms.TextInput(
        #         attrs={'placeholder': 'Username'}
        #     ),
        #     'email': forms.EmailInput(
        #         attrs={'placeholder': 'Email'}
        #     ),
        #     'building_code': forms.NumberInput(
        #         attrs={'placeholder': 'Building Code'}
        #     ),
        #     'password1': forms.PasswordInput(
        #         attrs={'placeholder': 'Password'}
        #     ),
        #     'password2': forms.PasswordInput(
        #         attrs={'placeholder': 'Confirm Password'}
        #     ),
        # }


        # field_classes = {'username': UsernameField}

class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )