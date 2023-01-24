from __future__ import annotations

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from ..libs import permission

from ..service import account_book_service, member_service


class AccountBookView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=128)
        description = serializers.CharField(max_length=256)

    def post(self, request):
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
