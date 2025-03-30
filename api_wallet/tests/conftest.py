import pytest

from wallets.models import Wallet


@pytest.fixture
def wallet():
    return Wallet.objects.create(amount=1000.00)


@pytest.fixture
def wallet_operation_url(wallet):
    return f'/api/v1/wallets/{wallet.id}/operation/'
