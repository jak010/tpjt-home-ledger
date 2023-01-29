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


@pytest.fixture
def accountbook_history(member_on, accountbook):
    accountbook_history = accountbook_service.create_account_book_history(
        amount=1000,
        memo="test",
        account_book=accountbook,
    )
    accountbook_history.is_active = 0
    accountbook_history.save()
    return accountbook_history


@pytest.mark.django_db
def test_accountsbooks_history_restore_api(client, auth_header, accountbook, accountbook_history):
    accountbooks_history_restore_view = reverse("application:accountbook_history_restore", kwargs={
        'accountbook_id': accountbook.reference_id,
        'accountbook_history_id': accountbook_history.reference_id
    })

    response = client.put(
        accountbooks_history_restore_view,
        **auth_header
    )

    assert response.status_code == 200
