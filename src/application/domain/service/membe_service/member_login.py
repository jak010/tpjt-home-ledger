from __future__ import annotations

from datetime import datetime

import pytz

from application.domain.exceptions import member_exception
from application.domain.repository.member_repository import MemberRepository
from application.libs import (
    utils,
    define
)


class MemberLogin:
    member_repository = MemberRepository()

    def __init__(self, email, password):
        self._email = email
        self._password = password

    def process(self):
        member = self.member_repository.get_member_by_email(
            member_email=self._email
        )

        self._password_check(
            input_password=self._password,
            store_password=member.password
        )
        self._is_active(member=member)

        member.last_login = datetime.now(tz=pytz.UTC)

        return member

    def _password_check(self, input_password, store_password):
        if not utils.check_password(input_password, store_password):
            raise member_exception.InvalidCredential()

    def _is_active(self, member):
        if member.is_active == define.Member.INACTIVE_CODE:
            raise member_exception.InActiveMember()
