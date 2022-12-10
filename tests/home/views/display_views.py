from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from home.models import Post

UserModel = get_user_model()


class TestBaseCase(TestCase):
    def assertEmpty(self, collection):
        return self.assertEqual(0, len(collection), 'It is not empty')

    def _create_user_and_login(self, user_data):
        user = UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        return user


class DisplayViewsTests(TestBaseCase):
    VALID_USER_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'testuser',
        'building_code': '1166',
        'email': 'testuser@mail.com',
        'password': 'thisisapassword12',
    }

    def test_no_posts_when_no_posts(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('posts page'))
        self.assertEmpty(response.context['posts'])

    def test_no_notifications_when_no_notifications(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('notifications'))
        self.assertEmpty(response.context['notifications'])

    def test_post_count_when_there_are_posts(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        posts = [Post(content='post content', user=user) for i in range(3)]
        for post in posts:
            post.save()

        response = self.client.get(reverse_lazy('posts page'))

        self.assertEqual(3, len(response.context['posts']))

    def test_make_post_template_renders(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('make post'))
        self.assertTemplateUsed(response, 'partials/make-post.html')

    def test_make_post_post_request(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        data = {
            'content': 'post content',
            'user': 'user',
        }
        response = self.client.post(reverse_lazy('make post'), data)
        self.assertRedirects(response, '/home/')
