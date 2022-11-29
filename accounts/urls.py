from django.urls import path

from accounts.views import UserRegisterView, UserLoginView, UserLogoutView, AdminUserRegisterView, \
    AdminUserLoginView, ProfileDetailsView, ProfileEditView, change_password, DeleteProfileView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register-admin/', AdminUserRegisterView.as_view(), name='register admin'),
    path('login-admin/', AdminUserLoginView.as_view(), name='login admin'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name="profile page"),

    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name="edit profile"),
    path('profile/<int:pk>/change-password/', change_password, name='change password'),
    path('profile/<int:pk>/delete/', DeleteProfileView.as_view(), name="delete profile"),
)
