import pytest

from django.shortcuts import reverse

from application.libs import utils

auth_logout_view = reverse("application:logout")


@pytest.mark.django_db
def test_member_logout_api(client,member_on_login):
    response = client.delete(
        auth_logout_view,
        **{'HTTP_ACCESS_TOKEN':member_on_login.token}
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_member_logout_api_with_invalid_token(client,member_on_login):
    response = client.delete(
        auth_logout_view,
        **{'HTTP_ACCESS_TOKEN':utils.generate_token(email="test_99999@test.com")}
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_member_logout_api_with_without_token(client,member_on_login):
    response = client.delete(
        auth_logout_view,
    )

    assert response.status_code == 403
