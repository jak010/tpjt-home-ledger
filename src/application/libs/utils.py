import bcrypt


def generate_bcrypt_hash(password) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(input_password: str, save_password: bytes) -> bool:
    return bcrypt.checkpw(
        input_password.encode("utf8"),
        save_password
    )
