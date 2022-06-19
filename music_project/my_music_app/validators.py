from django.core.exceptions import ValidationError


def username_validator(value):
    for letter in value:
        if not letter.isalnum() and not letter == '_':
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def positive_num_validator(value):
    if value < 0:
        raise ValidationError('Price cannot be below 0.0')
