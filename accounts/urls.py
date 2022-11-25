from django.urls import path

from accounts.views import register, login, register_admin, login_admin, profile_page, edit_profile_page, \
    delete_profile_page

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('register-admin/', register_admin, name='register admin'),
    path('login-admin/', login_admin, name='login admin'),
    path('profile/', profile_page, name="profile page"),
    path('profile/edit/', edit_profile_page, name="edit profile page"),
    path('profile/delete/', delete_profile_page, name="delete profile page"),
)