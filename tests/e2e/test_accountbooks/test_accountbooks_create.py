import pytest

from django.shortcuts import reverse

accountsbook_view = reverse("application:accountbooks")


@pytest.mark.django_db
def test_accountsbooks_create_api(client, auth_header):
    response = client.post(
        accountsbook_view,
        data={
            'name': "test accountbooks",
            'description': 'test description'
        },
        **auth_header
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_accountsbooks_create_api_without_inputdata(client, auth_header):
    response = client.post(
        accountsbook_view,
        data={},
        **auth_header
    )

    assert response.status_code == 400
