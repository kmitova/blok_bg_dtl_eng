from django.contrib import admin
from django.contrib.auth.models import Permission

from accounts.models import AppUser

admin.site.register(Permission)

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
# UserModel = get_user_model()

# @admin.register(UserModel)
# class UserAdmin(auth_admin.UserAdmin):
#     # form = UserEditForm
#     add_form = UserCreateForm


