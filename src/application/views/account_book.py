from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from ..libs import permission

from ..service import account_book_service, member_service

if TYPE_CHECKING:
    from src.config.types import APIResponse
    from ..exceptions import member_exception


class AccountBookView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        description = serializers.CharField(max_length=256)

    def get(self, request) -> APIResponse[
        Response
    ]:
        member = member_service.get_member_by_session(
            session=self.headers['member_session']
        )

        account_books = account_book_service.get_account_books(member=member)

        return Response(data=dict(
            summary=dict(
                count=len(account_books)
            ),
            items=[{
                'reference_id': account_book.reference_id,
                'name': account_book.name,
                'description': account_book.description,
                'date_of_create': account_book.date_of_create,  # TODO: KST로 시간대 변경 필요함
                'date_of_update': account_book.date_of_update
            } for account_book in account_books]
        ))

    def post(self, request) -> APIResponse[
        Response,
        member_exception.DoesNotExsitEmail
    ]:
        """ Acount Book 생성하기 """
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        member = member_service.get_member_by_session(
            session=self.headers['member_session']
        )

        account_book_service.create_account_book(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            member=member
        )

        return Response(status=200)
