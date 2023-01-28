import pytest

from application.service import member_service
from application.libs import utils


@pytest.fixture
def django_db_setup():
    """Avoid creating/setting up the test database"""
    pass


@pytest.fixture
def db_no_rollback(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)


@pytest.fixture
def member_on():
    member = member_service.create_member(
        email="test9999@test.com",
        password="1234"
    )

    return member


@pytest.fixture
def member_on_login(member_on):
    member = member_service.login(
        email=member_on.email,
        password="1234"
    )

    new_session = member_service.save_session(
        token=utils.generate_token(email=member.email),
        member=member
    )

    return new_session


@pytest.fixture
def auth_header(member_on_login):
    return {"HTTP_ACCESS_TOKEN": member_on_login.token}
