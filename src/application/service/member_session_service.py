from __future__ import annotations

from datetime import datetime
from typing import Optional, Generic, TYPE_CHECKING, TypeVar

import pytz
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from ..exceptions import member_exception
from ..libs import define, utils
from ..orm.member_session import MemberSession

from config.types import DjangoModel

Member: _MeberModel = get_user_model()

UTCNOW = datetime.now(tz=pytz.UTC)


class MemberSessionService:

    def __init__(self):
        self.model: MemberSession = Member

    def save_session(self, token: str, member: Member) -> MemberSession:
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

    def get_session(self, session_id) -> Optional[MemberSession]:
        """ session 정보 얻기 """
        try:
            member_session = MemberSession.objects.get(
                session_id=session_id
            )
        except MemberSession.DoesNotExist:
            raise member_exception.InvalidAccessToken()

        return member_session
