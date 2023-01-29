from __future__ import annotations

from rest_framework import permissions
from rest_framework import exceptions

from ..service.member_service import MemberService
from ..service.member_session_service import MemberSessionService

from ..libs import utils


class AccessTokenCheck(permissions.BasePermission):
    member_session_service = MemberSessionService()

    def has_permission(self, request, view):
        access_token = request.META.get("HTTP_ACCESS_TOKEN")

        if access_token is None:
            raise exceptions.PermissionDenied()

        decode_token = utils.decode_token(token=access_token)

        member_session = self.member_session_service.get_session(
            session_id=decode_token['session_id']
        )

        view.headers['member_session'] = member_session

        return True
