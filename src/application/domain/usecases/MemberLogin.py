from __future__ import annotations

from ..service.member_service import MemberService
from application.domain.exceptions import member_exception
from ..repository.member_repository import MemberRepository

from application.libs import (
    utils,
    define
)

from datetime import datetime
import pytz


class MemberLogin:

    def __init__(self, email, password):
        self._email = email
        self._password = password

        self.member_servce = MemberService()
        self.member_repository = MemberRepository()

    def _password_check(self, member, password):
        if not utils.check_password(password, member.password):
            raise member_exception.InvalidCredential()

    def _is_active(self, member):
        if member.is_active == define.Member.INACTIVE_CODE:
            raise member_exception.InActiveMember()

    def process(self):

        member = self.member_repository.get_member_by_email(
            member_email=self._email
        )
        member.last_login = datetime.now(tz=pytz.UTC)
