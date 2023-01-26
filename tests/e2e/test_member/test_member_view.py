import pytest

from django.shortcuts import reverse

member_view = reverse("application:member")


@pytest.mark.django_db
def test_member_create_api(client):
    response = client.post(
        member_view,
        data={
            'email': "test9998@test.com",
            'password': '1234'
        }
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_member_create_api_with_duplicate_check(client, member_on):
    response = client.post(
        member_view,
        data={
            'email': "test9999@test.com",
            'password': '1234'
        }
    )

    result = response.json()

    assert response.status_code == 200
    assert "20001, 이미 등록된 멤버가 존재합니다." in result['detail']
