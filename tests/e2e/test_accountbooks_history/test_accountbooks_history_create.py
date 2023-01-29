import pytest
from django.shortcuts import reverse

from application.service import accountbook_service


@pytest.fixture
def accountbook(member_on):
    return accountbook_service.create_account_book(
        name="test",
        description="test",
        member=member_on
    )


@pytest.mark.django_db
def test_accountsbooks_history_create_api(client, auth_header, accountbook):
    accountbooks_history_create_view = reverse("application:accountbooks_history_create", kwargs={
        'accountbook_id': accountbook.reference_id
    })

    response = client.post(
        accountbooks_history_create_view,
        data={
            'memo': "test accountbooks history",
            'amount': 1000
        },
        **auth_header
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_accountsbooks_history_create_api_without_data(client, auth_header, accountbook):
    accountbooks_history_create_view = reverse("application:accountbooks_history_create", kwargs={
        'accountbook_id': accountbook.reference_id
    })

    response = client.post(
        accountbooks_history_create_view,
        **auth_header
    )

    assert response.status_code == 400
