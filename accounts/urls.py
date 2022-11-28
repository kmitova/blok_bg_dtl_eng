from django.urls import path

from accounts.views import profile_page, \
    delete_profile_page, UserRegisterView, UserLoginView, UserLogoutView, AdminUserRegisterView, \
    AdminUserLoginView, ProfileDetailsView, ProfileEditView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register-admin/', AdminUserRegisterView.as_view(), name='register admin'),
    path('login-admin/', AdminUserLoginView.as_view(), name='login admin'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name="profile page"),
    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name="edit profile"),
    path('profile/<int:pk>/delete/', delete_profile_page, name="delete profile"),
)