from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from application.domain.repository.member_repository import MemberRepository

if TYPE_CHECKING:
    from application.domain.orm.member import Member


class MemberCreate:

    @cached_property
    def repository(self) -> MemberRepository:
        return MemberRepository()

    def process(self, email: str, password: str) -> Member:
        """ 멤버 생성하기 """
        return self.repository.add(
            email=email,
            password=password
        )
