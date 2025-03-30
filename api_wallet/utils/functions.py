from uuid import UUID

from rest_framework.exceptions import ValidationError

from utils.constants import INVALID_UUID_MESSAGE, UUID_VERSION


def uuid_verification(pk):
    """Проверяет соответствие pk кошелька формату UUID"""
    try:
        UUID(pk, version=UUID_VERSION)
    except ValueError:
        raise ValidationError(
            detail=INVALID_UUID_MESSAGE
        )
