from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..libs import permission
from ..service import accountbook_service
from ..service.member_service import MemberService
from ..service.member_session_service import MemberSessionService

if TYPE_CHECKING:
    from src.config.types import APIResponse
    from ..exceptions import member_exception


class AccountsBookView(APIView):
    member_service = MemberService()
    member_session_service = MemberSessionService()

    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        description = serializers.CharField(max_length=256)

    def get(self, request) -> APIResponse[
        Response,
        member_exception.InvalidCredential
    ]:
        """ 가계부 목록조회 """
        member = self.member_service.get_member_by_session(
            session=self.headers['member_session']
        )

        account_books = accountbook_service.get_account_books(member=member)

        return Response(data=account_books)

    def post(self, request) -> APIResponse[
        Response,
        member_exception.InvalidCredential
    ]:
        """ 가계부 생성하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        member = self.member_service.get_member_by_session(
            session=self.headers['member_session']
        )

        accountbook_service.create_account_book(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            member=member
        )

        return Response(status=201)


class AccountBookDetailView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    def get(self, request, accountbook_id) -> APIResponse[
        Response
    ]:
        """ 가계부 상세보기 """
        account_book_with_history = accountbook_service \
            .get_account_book_with_history(accountbook_id)

        return Response(data=account_book_with_history)
