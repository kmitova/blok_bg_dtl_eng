from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    # MAX_CONTENT_LEN = 1000
    MIN_CONTENT_LEN = 2

    content = models.TextField(
        # max_length=MAX_CONTENT_LEN,
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

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )


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
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT,)

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
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

    class Meta:
        ordering = ['publication_date']