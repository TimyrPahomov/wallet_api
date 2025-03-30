import uuid

from django.core.validators import MinValueValidator
from django.db import models

from utils.constants import (
    DECIMAL_PLACES,
    INVALID_AMOUNT_MESSAGE,
    MAX_DIGITS,
    MIN_AMOUNT
)


class Wallet(models.Model):
    """Класс для представления кошелька."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(
        'Сумма',
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=MIN_AMOUNT,
        validators=(
            MinValueValidator(MIN_AMOUNT, message=INVALID_AMOUNT_MESSAGE),
        )
    )
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(
        'Время последнего обновления', auto_now_add=False, auto_now=True
    )

    class Meta:
        verbose_name = 'кошелёк'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f"Кошелёк {self.id}"

    def operation_type(self):
        pass
