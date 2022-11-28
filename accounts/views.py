from django.contrib.auth import get_user_model, logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, UpdateView

# from django.shortcuts import render_to_response
from accounts.forms import UserCreateForm, UserLoginForm, AdminUserLoginForm, AdminUserCreateForm, DeleteProfileForm
from core.utils import get_date_joined

UserModel = get_user_model()
# def register(request):
#     return render(request, 'accounts/register.html')


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')


class AdminUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AdminUserCreateForm
    template_name = 'accounts/register-admin.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('home page')


class AdminUserLoginView(auth_views.LoginView):
    form_class = AdminUserLoginForm
    template_name = 'accounts/login-admin.html'
    next_page = reverse_lazy('home page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('landing page')


class ProfileDetailsView(DetailView):
    template_name = 'accounts/profile-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_owner'] = self.request.user == self.object
        # context['pets_count'] = self.object.pet_set.count()
        # photos = self.object.photo_set.prefetch_related('photolike_set')
        # context['photos_count'] = photos.count()
        # context['likes_count'] = sum([x.photolike_set.count() for x in photos])
        """
        date joined, name, number of posts, flat number, blok number
        """

        context['blok_number'] = str(self.object.building_code)[2:]
        context['date_joined'] = get_date_joined(self.object.date_joined)
        print(context)
        return context


class ProfileEditView(UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'password', 'apartment_number', 'profile_picture', 'username')

    def get_success_url(self):
        return reverse_lazy('profile page', kwargs={
            'pk': self.request.user.pk
        })

# def login(request):
#     return render(request, 'accounts/login.html')


# def register_admin(request):
#     return render(request, 'accounts/register-admin.html')
#
#
# def login_admin(request):
#     return render(request, 'accounts/login-admin.html')


def profile_page(request):
    return render(request, 'accounts/profile-page.html')


# def edit_profile_page(request, pk):
#     return render(request, 'accounts/edit-profile.html')

def get_profile(to_delete_pk):
    try:
        return UserModel.objects.filter(pk=to_delete_pk).get()
    except UserModel.DoesNotExist as e:
        return None

def delete_profile_page(request, pk):

    profile = get_profile(pk)
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('landing page')

    context = {
        'form': form,
    }

    return render(
        request,
        'accounts/verify-page.html',
        context,
    )


