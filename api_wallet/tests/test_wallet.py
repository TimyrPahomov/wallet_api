import uuid
from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_wallet_availability(client, wallet):
    url = f'/api/v1/wallets/{wallet.id}/'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_wallet_deposit_operation(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'operation_type': 'DEPOSIT',
        'amount': 1000
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.OK
    wallet.refresh_from_db()
    assert wallet.amount == 2000.00


@pytest.mark.django_db
def test_wallet_withdraw_operation(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'operation_type': 'WITHDRAW',
        'amount': 700.00
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.OK
    wallet.refresh_from_db()
    assert wallet.amount == 300.00


@pytest.mark.django_db
def test_wallet_withdraw_operation_insufficient_funds(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'operation_type': 'WITHDRAW',
        'amount': 2000.00
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    wallet.refresh_from_db()
    assert wallet.amount == 1000.00


@pytest.mark.django_db
def test_wallet_availability_with_invalid_uuid(
    client,
    wallet
):
    invalid_uuid = str(wallet.id)[1:]
    url = f'/api/v1/wallets/{invalid_uuid}/'
    response = client.get(url)
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.django_db
def test_wallet_operation_without_operation_type(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'amount': 700.00
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    wallet.refresh_from_db()
    assert wallet.amount == 1000.00


@pytest.mark.django_db
def test_wallet_operation_without_amount(
    client,
    wallet_operation_url
):
    data = {
        'operation_type': 'DEPOSIT'
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.django_db
def test_wallet_operation_with_invalid_operation_type(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'operation_type': 'deposit',
        'amount': 1000.00
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    wallet.refresh_from_db()
    assert wallet.amount == 1000.00


@pytest.mark.django_db
def test_wallet_operation_with_invalid_amount(
    client,
    wallet,
    wallet_operation_url
):
    data = {
        'operation_type': 'DEPOSIT',
        'amount': -1000
    }
    response = client.post(
        wallet_operation_url,
        data,
        format='json'
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    wallet.refresh_from_db()
    assert wallet.amount == 1000.00


@pytest.mark.django_db
def test_wallet_not_exist(client):
    not_exist_wallet = str(uuid.uuid4())
    url = f'/api/v1/wallets/{not_exist_wallet}/'
    response = client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND
