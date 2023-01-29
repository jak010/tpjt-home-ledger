import pytest
from django.db.utils import IntegrityError

from application import errors

from src.application.libs import utils


@pytest.mark.django_db
def test_member_login(member_on, member_service, member_session_service):
    member_session_service.save_session(
        member=member_on,
        token=utils.generate_token(member_on.email)
    )


@pytest.mark.django_db
def test_member_login_without_member(member_on, member_service, member_session_service):
    # django.db.utils.IntegrityError: (1048, "Column 'member_id' cannot be null")
    with pytest.raises(IntegrityError):
        member_session_service.save_session(
            member=None,
            token=utils.generate_token(member_on.email)
        )


@pytest.mark.django_db
def test_member_login_without_token(member_on, member_service, member_session_service):
    with pytest.raises(errors.TokenDecodeError):
        member_session_service.save_session(
            member=member_on,
            token=None
        )
