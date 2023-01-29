from __future__ import annotations

from datetime import datetime
from typing import Optional

import pytz
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from ..exceptions import member_exception
from ..libs import define,utils
from ..orm.member_session import MemberSession

Member = get_user_model()

UTCNOW = datetime.now(tz=pytz.UTC)


def create_member(email: str,password: str) -> Member:
    """ Member 생성하기 """
    try:
        member = Member.objects.create(
            email=email,
            password=utils.generate_bcrypt_hash(password)
        )
        member.full_clean()
    except IntegrityError:
        raise member_exception.AlreadyExistMember()

    return member


def login(email: str,password: str) -> Member:
    """ 멤버 로그인 """
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        raise member_exception.InvalidCredential()

    if not utils.check_password(password,member.password):
        raise member_exception.InvalidCredential()

    if member.is_active == define.Member.INACTIVE_CODE:
        raise member_exception.InActiveMember()

    member.last_login = UTCNOW
    member.save()

    return member


def save_session(token: str,member: Member) -> MemberSession:
    """ token 정보 저장하기 """
    decode_token = utils.decode_token(token)

    new_session = MemberSession.objects.create(
        session_id=decode_token['session_id'],
        token=token,
        member=member,
        expire_time=decode_token['exp'],
        iat_time=decode_token['iss']
    )
    return new_session


def get_session(session_id) -> Optional[MemberSession]:
    """ session 정보 얻기 """
    try:
        member_session = MemberSession.objects.get(
            session_id=session_id
        )
    except MemberSession.DoesNotExist:
        raise member_exception.InvalidAccessToken()

    return member_session


def get_member_by_session(session: MemberSession) -> Member:
    token = utils.decode_token(session.token)

    try:
        member = Member.objects.get(
            email=token['email']
        )
    except Member.DoesNotExist:
        raise member_exception.InvalidCredential()

    return member


def get_member_with_email(email: str) -> Member:
    try:
        member = Member.objects.get(email=email)

    except Member.DoesNotExist:
        raise member_exception.DoesNotExsitEmail()

    return member
