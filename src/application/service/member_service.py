from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from ..exceptions import member_exception
from ..libs import utils, define

from datetime import datetime

from ..orm.member_session import MemberSession

# from ..orm.member_session import MemberSession

Member = get_user_model()


def create_member(email: str, password: str) -> Member:
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


def login(email: str, password: str) -> Member:
    """ 멤버 로그인 """
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist as e:
        raise member_exception.InvalidCredential()

    if not utils.check_password(password, member.password.encode()):
        raise member_exception.InvalidCredential()

    if member.is_active == define.Member.INACTIVE_CODE:
        raise member_exception.InActiveMember()

    member.last_login = datetime.now()
    member.save()

    return member


def save_token(token: str, member: Member) -> MemberSession:
    token = utils.decode_token(token)

    new_session = MemberSession.objects.create(
        session_id=token['session_id'],
        token=token,
        member=member,
        expire_date=token['exp'],
        iat=token['iss']
    )
    return new_session
