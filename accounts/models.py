
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from core.validators import validate_building_code_length


class AppUser(AbstractUser):

    NAME_MAX_LEN = 45
    NAME_MIN_LEN = 2

    # building code validator
    # admin code validator

    # first_name = models.CharField()
    # last_name = models.CharField()
    # email = models.EmailField()
    # building_code = models.IntegerField()
    # profile_picture = models.ImageField()
    # is_admin = models.BooleanField()
    # admin_code = models.IntegerField()

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=True
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=True
    )

    # is_active = models.BooleanField(default=True)

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    building_code = models.IntegerField(
        validators=(
            validate_building_code_length,
        ),
        null=False,
        blank=False,
    )

    is_admin = models.BooleanField(
        null=True,
        blank=True,
        default=False
    )

    admin_code = models.IntegerField(
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='images/',
        # default='images/default_profile_pic.png',
        null=True,
        blank=True,
    )
