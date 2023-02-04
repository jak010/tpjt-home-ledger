import pytest

from application.domain.service.membe_service import MemberCreate, MemberLogin
from application.domain.service.member_session_service import MemberSessionService
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
    return MemberCreate().process(
        email="test9999@test.com",
        password="1234"
    )


@pytest.fixture
def member_login_serivce():
    return MemberLogin


@pytest.fixture
def member_session_service():
    return MemberSessionService()


@pytest.fixture
def member_on_login(member_on, member_login_serivce, member_session_service):
    member = member_login_serivce(
        email=member_on.email,
        password="1234"
    ).process()

    new_session = member_session_service.save_session(
        token=utils.generate_token(email=member.email),
        member=member
    )

    return new_session


@pytest.fixture
def auth_header(member_on_login):
    return {"HTTP_ACCESS_TOKEN": member_on_login.token}
