import pytest
from django.shortcuts import reverse

from application.service import accountbook_service

accountsbook_view = reverse("application:accountbooks")


@pytest.fixture
def create_accountbooks(member_on):
    accountbook_service.create_account_book(
        name="test",
        description="test",
        member=member_on
    )


@pytest.mark.django_db
def test_accountsbooks_list_api(client,auth_header,create_accountbooks):
    response = client.get(
        accountsbook_view,
        **auth_header
    )

    result = response.json()['items'][0]

    assert response.status_code == 200

    assert 'reference_id' in result
    assert 'name' in result
    assert 'description' in result
    assert 'date_of_create' in result
    assert 'date_of_update' in result
