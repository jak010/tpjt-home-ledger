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
def accountbook_history(member_on,accountbook):
    return accountbook_service.create_account_book_history(
        amount=1000,
        memo="test",
        account_book=accountbook
    )


@pytest.mark.django_db
def test_accountsbooks_history_delete_api(client,auth_header,accountbook,accountbook_history):
    accountbooks_history_update_view = reverse("application:accountbook_history_detail",kwargs={
        'accountbook_id':accountbook.reference_id,
        'accountbook_history_id':accountbook_history.reference_id
    })

    response = client.delete(
        accountbooks_history_update_view,
        data={
            'amount':1000,
            'memo':"test accountbooks history",
        },
        content_type="application/json",  # HACK: 처리 안해주면 415 Status 발생
        **auth_header
    )

    assert response.status_code == 200
