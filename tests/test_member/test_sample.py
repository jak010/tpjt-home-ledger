import pytest

from django.contrib.auth import get_user_model

Member = get_user_model()


def test_create_member(db_no_rollback) -> None:
    email = "bluetoon@naver.com"
    password = 1234

    member = Member.objects.create(email=email, password=password)
