import pytest
from django.shortcuts import reverse

from application.domain.service import accountbook_service


@pytest.fixture
def create_accountbooks(member_on):
    return accountbook_service.create_account_book(
        name="test",
        description="test",
        member=member_on
    )


@pytest.mark.django_db
def test_accountsbooks_retrieve_api(client, auth_header, create_accountbooks):
    view = reverse("application:accountbooks_detail", kwargs={
        'accountbook_id': int(create_accountbooks.reference_id)
    })

    response = client.get(
        view,
        **auth_header
    )

    result = response.json()

    assert response.status_code == 200

    assert 'reference_id' in result['account_book']
    assert 'name' in result['account_book']
    assert 'description' in result['account_book']
    assert 'date_of_create' in result['account_book']
    assert 'date_of_update' in result['account_book']

    if result['historys']:
        history = result['historys'][0]
        assert 'reference_id' in history
        assert 'memo' in history
        assert 'date_of_create' in history
        assert 'date_of_update' in history
