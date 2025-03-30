from rest_framework import serializers

from utils.constants import CHOICES
from wallets.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с кошельками.

    Вызывается для изменения баланса кошелька.
    """

    operation_type = serializers.ChoiceField(choices=CHOICES, write_only=True)

    class Meta:
        model = Wallet
        fields = ('amount', 'operation_type')
        extra_kwargs = {'amount': {'required': True}}
