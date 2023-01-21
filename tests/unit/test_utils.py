from src.application.libs import utils

TEST_PASSWORD = "1234"


def test_generate_bcrypt_hash():
    new_bcrypt = utils.generate_bcrypt_hash(TEST_PASSWORD)

    assert isinstance(new_bcrypt, bytes)


def test_check_password_success():
    new_bcrypt = utils.generate_bcrypt_hash(TEST_PASSWORD)

    check_passwod = utils.check_password(TEST_PASSWORD, new_bcrypt)

    assert check_passwod is True


def test_check_password_failure():
    new_bcrypt = utils.generate_bcrypt_hash(TEST_PASSWORD)

    check_passwod = utils.check_password("4321", new_bcrypt)

    assert check_passwod is False
