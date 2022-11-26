from django.urls import path

from accounts.views import register_admin, login_admin, profile_page, edit_profile_page, \
    delete_profile_page, UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register-admin/', register_admin, name='register admin'),
    path('login-admin/', login_admin, name='login admin'),
    path('profile/', profile_page, name="profile page"),
    path('profile/edit/', edit_profile_page, name="edit profile page"),
    path('profile/delete/', delete_profile_page, name="delete profile page"),
)