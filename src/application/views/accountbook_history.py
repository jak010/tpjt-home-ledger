from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import exceptions
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from application.domain.exceptions import accountbook_exception
from application.domain.service.member_service import MemberService
from application.domain.service.member_session_service import MemberSessionService
from application.libs.define import AccountHistoryStatus
from config import permission
from ..domain.service import accountbook_service

if TYPE_CHECKING:
    from src.config.types import APIResponse


class AccountBookHistoryCreateView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        memo = serializers.CharField(max_length=256, required=True)
        amount = serializers.CharField(max_length=128, required=True)

    def post(self, request, accountbook_id) -> APIResponse[
        Response,
        accountbook_exception.DoesNotExsitAccountBook,
    ]:
        """ Acount Book History 생성하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account_book = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )

        accountbook_service.create_account_book_history(
            account_book=account_book,
            amount=serializer.validated_data['amount'],
            memo=serializer.validated_data['memo'],
        )

        return Response(status=201)


class AccountBookHistoryDetailView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        memo = serializers.CharField(max_length=256, required=True)
        amount = serializers.IntegerField(required=True)

    def put(self, request, accountbook_id, accountbook_history_id) -> APIResponse[
        Response,
        accountbook_exception.DoesNotExsitAccountBook,
        accountbook_exception.DoesNotExsitAccountHistoryBook,
        accountbook_exception.InActivedAccountbookHistory
    ]:
        """ Acount Book History 수정하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        accountbook = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )

        accountbook_history = accountbook_service.get_acoount_book_history(
            accountbook_history_id=accountbook_history_id,
            accountbook=accountbook,
        )

        accountbook_service.update_account_book_history(
            account_book_history=accountbook_history,
            amount=serializer.validated_data['amount'],
            memo=serializer.validated_data['memo']
        )

        return Response(status=200)

    def delete(self, request, accountbook_id, accountbook_history_id) -> APIResponse[
        Response,
        accountbook_exception.DoesNotExsitAccountHistoryBook,
        accountbook_exception.InActivedAccountbookHistory
    ]:
        """ 가계부 내역 삭제하기 """
        accountbook = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )

        account_book_history = accountbook_service.get_acoount_book_history(
            accountbook_history_id=accountbook_history_id,
            accountbook=accountbook
        )
        account_book_history.is_active = 0
        account_book_history.save()

        return Response(status=200)


class AccountBookHistoryRestoreView(APIView):
    member_service = MemberService()
    member_session_service = MemberSessionService()

    permission_classes = (permission.AccessTokenCheck,)

    def put(self, request, accountbook_id, accountbook_history_id) -> APIResponse[Response]:
        account_book = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )
        member = self.member_service.get_member_by_session(
            session=self.headers['member_session']
        )

        if account_book.author.id != member.id:
            raise exceptions.PermissionDenied()

        account_book_history = accountbook_service.get_account_book_history_without_status(
            reference_id=accountbook_history_id
        )
        if account_book_history.is_active == AccountHistoryStatus.active.value:
            raise accountbook_exception.AlreadyActivedAccountbookHistory()

        account_book_history.is_active = AccountHistoryStatus.active.value
        account_book_history.save()

        return Response(200)
