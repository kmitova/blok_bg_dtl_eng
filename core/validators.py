import datetime

from django.core import exceptions


def validate_building_code_length(value):
    if not len(str(value)) >= 4:
        raise exceptions.ValidationError('Invalid code length!')


def check_card_date_expiry(given_date):
    if given_date < datetime.datetime.today().date():
        raise exceptions.ValidationError('Invalid expiry date!')

