from django.db import models


class Fee(models.Model):
    fee = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )

    deadline = models.DateField(
        null=False,
        blank=False
    )
