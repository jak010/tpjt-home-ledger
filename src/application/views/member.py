from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..exceptions.member_exception import AlreadyExistMember
from ..service.member_service import MemberService

if TYPE_CHECKING:
    from src.config.types import APIResponse


class MemberView(APIView):
    member_service = MemberService()

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)

    def post(self, *args, **kwags) -> APIResponse[
        Response,
        AlreadyExistMember
    ]:
        """ Member 생성하기 """
        serializer = self.InputSerializer(data=self.request.POST)
        serializer.is_valid(raise_exception=True)

        self.member_service.create_member(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        return Response(status=201)
