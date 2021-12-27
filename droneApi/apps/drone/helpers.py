from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weight(value):
    if value < 0.0 or value > 500.0:
        raise ValidationError(
            _('%(value)s must be in the range [0.0, 500.0]'),
            params={'value': value},
        )


def validate_percentage(value):
    if value < 0.0 or value > 100.0:
        raise ValidationError(
            _('%(value)s must be in the range [0.0, 100.0]'),
            params={'value': value},
        )