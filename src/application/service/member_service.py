from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import pytz
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from rest_framework import exceptions

from ..exceptions import member_exception
from ..libs import define, utils
from ..orm.member_session import MemberSession

if TYPE_CHECKING:
    from ..orm.member import Member as _MeberModel

Member: _MeberModel = get_user_model()

UTCNOW = datetime.now(tz=pytz.UTC)


class MemberService:

    def __init__(self):
        self.model: _MeberModel = Member

    def get_member_by_id(self, reference_id) -> Member:
        try:
            member = self.model.manager.get(id=reference_id)
        except _MeberModel.DoesNotExsit:
            raise member_exception.InvalidCredential()

        return member

    def get_member_by_email(self, email) -> Member:
        try:
            member = self.model.manager.get(email=email)
        except _MeberModel.DoesNotExsit:
            raise member_exception.InvalidCredential()

        return member

    def get_member_by_session(self, session: MemberSession) -> Member:
        token = utils.decode_token(session.token)

        return self.get_member_by_email(email=token['email'])

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
        member = self.get_member_by_email(email=email)

        if not utils.check_password(password, member.password):
            raise member_exception.InvalidCredential()

        if member.is_active == define.Member.INACTIVE_CODE:
            raise member_exception.InActiveMember()

        member.last_login = UTCNOW
        member.save()

        return member
