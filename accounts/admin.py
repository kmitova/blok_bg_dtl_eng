from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from accounts.forms import UserCreateForm
from accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
# UserModel = get_user_model()

# @admin.register(UserModel)
# class UserAdmin(auth_admin.UserAdmin):
#     # form = UserEditForm
#     add_form = UserCreateForm


