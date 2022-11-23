from django.urls import path

from accounts.views import register, login, register_admin, login_admin

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('register-admin/', register_admin, name='register admin'),
    path('login-admin/', login_admin, name='login admin'),
)