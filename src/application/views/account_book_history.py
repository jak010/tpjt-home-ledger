from __future__ import annotations

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from ..libs import permission

from ..service import account_book_service


class AccountBookHistoryView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        memo = serializers.CharField(max_length=256, required=True)
        amount = serializers.CharField(max_length=128, required=True)

    def post(self, request, account_book_id):
        """ Acount Book History 생성하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account_book = account_book_service.get_account_book_with_pk(
            reference_id=account_book_id
        )

        account_book_service.create_account_book_history(
            account_book=account_book,
            amount=serializer.validated_data['amount'],
            memo=serializer.validated_data['memo'],
        )

        return Response(status=200)
