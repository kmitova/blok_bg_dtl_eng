from django.contrib.auth import get_user_model

from home.models import Post


def get_date_joined(date):
    current_date = date
    current_date_no_time = current_date.strftime('%d.%m.%Y')
    return current_date_no_time


UserModel = get_user_model()


def get_building_code(request):
    current_user = request.user
    current_building_code = current_user.building_code
    return current_building_code


def get_group_posts(request):
    current_building_code = get_building_code(request)
    posts = Post.objects.filter(user__building_code=current_building_code)
    return posts


def get_group_users(request):
    current_building_code = get_building_code(request)
    users = UserModel.objects.filter(building_code=current_building_code)
    return users


