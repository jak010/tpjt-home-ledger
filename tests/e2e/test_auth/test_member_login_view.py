import pytest

from django.shortcuts import reverse

auth_login_view = reverse("application:login")


@pytest.mark.django_db
def test_member_login_api(client,member_on):
    response = client.post(
        auth_login_view,
        data={
            'email':member_on.email,
            'password':'1234'
        }
    )

    result = response.json()

    assert response.status_code == 201

    assert 'access_token' in result
    assert 'expire_time' in result
    assert 'iat_time' in result


@pytest.mark.django_db
def test_member_login_api_with_fail(client,member_on):
    response = client.post(
        auth_login_view,
        data={
            'email':member_on.email,
            'password':'12345'
        }
    )

    assert response.status_code == 400
