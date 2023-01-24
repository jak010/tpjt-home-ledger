import bcrypt
import uuid


def generate_bcrypt_hash(password) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(input_password: str, save_password: bytes) -> bool:
    return bcrypt.checkpw(
        input_password.encode("utf8"),
        save_password
    )


def generate_session_id():
    return str(uuid.uuid4())[0:32]
