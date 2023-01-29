from __future__ import annotations

from datetime import datetime
from typing import TypedDict

from ..orm.member import Member


class TokenClaim(TypedDict):
    session_id: str
    member: Member
    token: str
    expire_date: datetime
    iat_date: datetime
