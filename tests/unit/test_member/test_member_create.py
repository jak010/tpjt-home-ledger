import pytest
from django.core.exceptions import ValidationError
from django.db.utils import DataError

from application.service.member_service import MemberService


@pytest.mark.django_db
def test_member_create():
    input_email = "test_100000@test.com"
    input_password = '1234'

    member = MemberService().create_member(
        email=input_email,
        password=input_password
    )

    assert member.email == input_email


@pytest.mark.django_db
def test_member_create_with_invalid_email():
    input_email = "test_100000test.com"
    input_password = '1234'

    with pytest.raises(ValidationError):
        MemberService().create_member(
            email=input_email,
            password=input_password
        )


@pytest.mark.django_db
def test_member_create_with_max_input():
    input_email = "test_100000" * 100 + "@test.com"
    input_password = '1234'

    with pytest.raises(DataError):
        MemberService().create_member(
            email=input_email,
            password=input_password
        )
