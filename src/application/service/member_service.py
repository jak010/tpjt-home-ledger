from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import pytz
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from ..exceptions import member_exception
from ..libs import define, utils
from ..orm.member_session import MemberSession

if TYPE_CHECKING:
    from ..orm.member import Member as _MeberModel

Member: _MeberModel = get_user_model()

UTCNOW = datetime.now(tz=pytz.UTC)


class MemberService:

    def __init__(self):
        self.model: MemberModel = Member

    def get_member_by_id(self, reference_id) -> Member:
        return Member.objects.get(
            id=reference_id
        )

    def create_member(self, email: str, password: str) -> Member:
        """ 멤버 생성하기 """
        try:
            member = self.model.manager.create(
                email=email,
                password=utils.generate_bcrypt_hash(password)
            )
            member.full_clean()
        except IntegrityError:
            raise member_exception.AlreadyExistMember()

        return member

    def login(self, email: str, password: str) -> Member:
        """ 멤버 로그인 """
        try:
            member = self.model.manager.get(email=email)
        except self.model.DoesNotExist:
            raise member_exception.InvalidCredential()

        if not utils.check_password(password, member.password):
            raise member_exception.InvalidCredential()

        if member.is_active == define.Member.INACTIVE_CODE:
            raise member_exception.InActiveMember()

        member.last_login = UTCNOW
        member.save()

        return member

    def get_member_by_session(self, session: MemberSession) -> Member:
        token = utils.decode_token(session.token)

        try:
            member = Member.manager.get(
                email=token['email']
            )
        except Member.DoesNotExist:
            raise member_exception.InvalidCredential()

        return member
