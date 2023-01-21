from __future__ import annotations

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers

from ..service import member_service


class MemberView(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, *args, **kwags):
        """ Member 생성하기 """
        serializer = self.InputSerializer(data=self.request.POST)
        serializer.is_valid(raise_exception=True)

        member_service.create_member(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        return Response(201)
