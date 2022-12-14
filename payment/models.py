from django.contrib.auth import get_user_model
from django.core import validators, exceptions
from django.db import models

from core.validators import check_card_date_expiry

UserModel = get_user_model()


class Fee(models.Model):
    fee = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        default=10,
    )

    deadline = models.DateField(
        null=False,
        blank=False
    )

    class Meta:
        ordering = ['-deadline']


class Payment(models.Model):

    CARD_LEN = 16
    CVV_LEN = 3

    card_number = models.CharField(
        max_length=CARD_LEN,
        validators=(validators.MinLengthValidator(CARD_LEN),),
        null=False,
        blank=False,
    )

    card_cvv = models.CharField(
        max_length=CVV_LEN,
        validators=(validators.MinLengthValidator(CVV_LEN),),
        null=False,
        blank=False,
    )

    card_expiry_date = models.DateField(
        validators=(check_card_date_expiry,),
        null=False,
        blank=False,
    )

    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, )

