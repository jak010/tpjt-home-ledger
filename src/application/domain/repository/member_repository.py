from __future__ import annotations

from application.domain import errors
from application.domain.exceptions import member_exception
from application.domain.orm.member_session import MemberSession
from application.libs import (
    utils
)
from ..orm.member import Member
from django.db.utils import IntegrityError


class MemberRepository:

    def get_member_by_pk(self, reference_id: int) -> Member:
        try:
            member = Member.manager.get(pk=reference_id)
        except Member.DoesNotExist:
            raise member_exception.NotExistsMember()

        return member

    def get_member_by_email(self, member_email: str) -> Member:
        try:
            member = Member.manager.get(email=member_email)
        except Member.DoesNotExist:
            raise member_exception.NotExistsMember()

        return member

    def get_member_by_session(self, session: MemberSession) -> Member:
        try:
            token = utils.decode_token(session.token)
        except errors.TokenDecodeError:
            raise member_exception.InvalidAccessToken()

        return self.get_member_by_email(member_email=token['email'])

    def add(self, email: str, password: str):
        try:
            new_member = Member(
                email=email,
                password=utils.generate_bcrypt_hash(password)
            )
            new_member.save()
        except IntegrityError:
            raise member_exception.AlreadyExistMember()

        return new_member
