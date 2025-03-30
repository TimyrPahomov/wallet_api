from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.serializers import WalletSerializer
from utils.functions import uuid_verification
from wallets.models import Wallet


class WalletViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Набор представлений для работы с кошельком."""

    serializer_class = WalletSerializer

    def get_queryset(self):
        """Возвращает баланс кошелька."""
        pk = self.kwargs.get('pk')
        uuid_verification(pk)
        return Wallet.objects.filter(pk=pk)

    @action(
        detail=True, methods=['post'], url_path='operation'
    )
    def operation(self, request, pk):
        """Отвечает за изменение счёта."""
        uuid_verification(pk)
        with transaction.atomic():
            wallet = get_object_or_404(
                Wallet.objects.select_for_update(), pk=pk
            )
            serializer = WalletSerializer(
                context={'request': request},
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            operation_type = serializer.validated_data.get('operation_type')
            amount = serializer.validated_data.get('amount')
            if operation_type == 'DEPOSIT':
                wallet.amount += amount
            elif operation_type == 'WITHDRAW':
                if wallet.amount < amount:
                    return Response(
                        'В кошельке недостаточно средств.',
                        status=status.HTTP_400_BAD_REQUEST
                    )
                wallet.amount -= amount
            wallet.save()
        return Response(
            f'Баланс кошелька: {wallet.amount}',
            status=status.HTTP_200_OK
        )
