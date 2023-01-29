from __future__ import annotations

import datetime
import time
import uuid
from typing import TYPE_CHECKING

import bcrypt
import jwt
from django.conf import settings

from .. import errors

if TYPE_CHECKING:
    pass


def generate_bcrypt_hash(password) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(input_password: str, save_password: str) -> bool:
    return bcrypt.checkpw(
        input_password.encode("utf8"),
        save_password.encode("utf8")
    )


def generate_session_id() -> str:
    return str(uuid.uuid4())


def datetime_to_epoch(day) -> int:
    _datetime = datetime.datetime.utcnow() + datetime.timedelta(days=day)
    return int(time.mktime(_datetime.timetuple()))


def generate_token(email: str) -> str:
    """ jwt 토큰 생성하기 """
    return jwt.encode(
        payload={
            'session_id': generate_session_id(),
            'email': email,
            'exp': datetime_to_epoch(day=1),
            'iss': datetime_to_epoch(day=2),
        },
        key=settings.SECRET_KEY,
        algorithm='HS256'
    )


def decode_token(token) -> dict:
    """ decode token """
    try:
        token = jwt.decode(
            jwt=token,
            key=settings.SECRET_KEY,
            algorithms='HS256'
        )
    except Exception:  # TODO: Token Deode 시 Exception 처리 명시하기
        raise errors.TokenDecodeError()

    return token
