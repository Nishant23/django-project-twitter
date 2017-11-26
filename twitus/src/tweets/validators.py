from __future__ import unicode_literals
from django.core.exceptions import ValidationError



def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Content can't be blank")
    return value
