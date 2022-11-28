from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from accounts.templatetags.custom_filters import placeholder

UserModel = get_user_model()


class DeleteProfileForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserModel
        fields = ('confirm_password',)
    def clean(self):
        cleaned_data = super(DeleteProfileForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')

    def save(self, commit=True):
        user = super(DeleteProfileForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            # TODO: delete all associated data as well (posts, comments, etc)
            self.instance.delete()

        return self.instance

class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')

    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user

class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email',
                  'building_code', 'password1', 'password2')


class AdminUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email',
                  'building_code', 'is_admin', 'admin_code',
                  'password1', 'password2')

        is_admin = forms.BooleanField(label="I confirm I am an admin.")
        # widgets = {
        #     'is_admin': forms.HiddenInput(
        #         attrs={
        #             'value': True
        #         }
        #     )
        # }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'}
    )


# class AdminUserLoginForm(forms.ModelForm):
#     # def __init__(self, *args, **kwargs):
#     #     self.request = kwargs.pop('request', None)
#     #     super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = UserModel
#         fields = ('username', 'admin_code', 'password')
#         widgets = {
#             'password': forms.PasswordInput()
#         }


class AdminUserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    # admin_code = forms.NumberInput(attrs={'placeholder': 'Admin Code'})
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )