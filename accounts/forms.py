from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from accounts.templatetags.custom_filters import placeholder

UserModel = get_user_model()


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('password',)

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


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