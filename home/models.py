from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    MIN_CONTENT_LEN = 2

    content = models.TextField(
        validators=(
            validators.MinLengthValidator(MIN_CONTENT_LEN),
        ),
        null=False,
        blank=False,
    )

    photo = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        blank=True,
        null=False,
        auto_now=True,
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )


class Comment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,)

    class Meta:
        ordering = ['publication_date']


class Reply(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = 'Replies'


class SupportPost(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Announcement(models.Model):
    title = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )


class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender')