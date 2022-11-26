from django.core import exceptions


def validate_building_code_length(value):
    if not len(str(value)) == 4:
        raise exceptions.ValidationError('Invalid code length!')
