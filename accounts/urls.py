from django.urls import path

from accounts.views import profile_page, edit_profile_page, \
    delete_profile_page, UserRegisterView, UserLoginView, UserLogoutView, AdminUserRegisterView, \
 AdminUserLoginView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register-admin/', AdminUserRegisterView.as_view(), name='register admin'),
    path('login-admin/', AdminUserLoginView.as_view(), name='login admin'),
    path('profile/', profile_page, name="profile page"),
    path('profile/edit/', edit_profile_page, name="edit profile page"),
    path('profile/delete/', delete_profile_page, name="delete profile page"),
)