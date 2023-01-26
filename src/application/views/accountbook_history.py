from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from ..libs import permission

from ..service import accountbook_service

if TYPE_CHECKING:
    from src.config.types import APIResponse
    from ..exceptions import member_exception, accountbook_exception


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
        amount = serializers.CharField(max_length=128, required=True)

    def put(self, request, accountbook_id, accountbook_history_id) -> APIResponse[
        Response,
        accountbook_exception.DoesNotExsitAccountBook,
        accountbook_exception.DoesNotExsitAccountHistoryBook,
        accountbook_exception.InActivedAccountbookHistory
    ]:
        """ Acount Book History 수정하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account_book = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )

        account_book_history = accountbook_service.get_acoount_book_history(
            reference_id=accountbook_history_id
        )

        accountbook_service.update_account_book_history(
            account_book_history=account_book_history,
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
        account_book = accountbook_service.get_account_book_with_pk(
            reference_id=accountbook_id
        )

        account_book_history = accountbook_service.get_acoount_book_history(
            reference_id=accountbook_history_id
        )
        account_book_history.is_active = 0
        account_book_history.save()

        return Response(status=200)
