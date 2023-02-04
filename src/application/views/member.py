from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from application.domain.exceptions.member_exception import AlreadyExistMember
from application.domain.service.membe_service import MemberCreate

if TYPE_CHECKING:
    from src.config.types import APIResponse


class MemberView(APIView):
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

        MemberCreate().process(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        return Response(status=201)


class MemberDetailView(APIView):

    def get(self, member_id: int):
        member = self.service.get_member_by_id(reference_id=member_id)

        return Response(
            status=200,
            data={
                'member_id': member.id
            }
        )
