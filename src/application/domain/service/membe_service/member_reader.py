from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from application.domain.orm.member_session import MemberSession
from application.domain.repository.member_repository import MemberRepository

if TYPE_CHECKING:
    from application.domain.orm.member import Member


class MemberReader:

    @cached_property
    def repository(self) -> MemberRepository:
        return MemberRepository()

    def get_member_by_id(self, reference_id: int) -> Member:
        return self.repository.get_member_by_pk(
            reference_id=reference_id
        )

    def get_member_by_email(self, email: str) -> Member:
        return self.repository.get_member_by_email(
            member_email=email
        )

    def get_member_by_session(self, session: MemberSession) -> Member:
        return self.repository.get_member_by_session(session=session)
