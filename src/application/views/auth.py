from __future__ import annotations

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from ..libs import permission
from ..libs import utils
from ..service.member_service import MemberService
from ..service.member_session_service import MemberSessionService


class LoginView(APIView):
    member_service = MemberService()
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

        member = self.member_service.login(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

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
    member_service = MemberService()

    permission_classes = (permission.AccessTokenCheck,)

    def delete(self, request):
        member_session = self.headers['member_session']

        member_session.delete()

        return Response(200)
