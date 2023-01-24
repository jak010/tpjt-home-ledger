import pytest

from application.service import member_service


@pytest.fixture
def django_db_setup():
    """Avoid creating/setting up the test database"""
    pass


@pytest.fixture
def db_no_rollback(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)


@pytest.fixture()
def member_on():
    member_service.create_member(
        email="test99@test.com",
        password="1234"
    )
