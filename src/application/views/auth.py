from __future__ import annotations

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from application.domain.service.membe_service.member_login import MemberLogin
from application.domain.service.member_session_service import MemberSessionService
from config import permission
from ..libs import utils


class LoginView(APIView):
    member_session_service = MemberSessionService()

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)

    def post(self, request):
        """ token 생성하기 """
        # email과 패스워드로 가입된 유저인지 검증
        # 가입된 유저이면 토큰을 생성함
        # 생성된 토큰 정보는 db에 저장

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        member_login = MemberLogin(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        member = member_login.process()

        new_session = self.member_session_service.save_session(
            token=utils.generate_token(email=member.email),
            member=member
        )

        return Response(
            status=201,
            data={
                'access_token': new_session.token,
                'expire_time': new_session.expire_time,
                'iat_time': new_session.iat_time
            }
        )


class LogOutView(APIView):
    permission_classes = (permission.AccessTokenCheck,)

    def delete(self, request):
        member_session = self.headers['member_session']

        member_session.delete()

        return Response(200)
