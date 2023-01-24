from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from rest_framework import serializers

from rest_framework.views import APIView
from ..service import member_service

from ..libs import utils


class LoginApiView(APIView):
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

        member = member_service.login(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        new_session = member_service.save_token(
            token=utils.generate_token(member=member),
            member=member
        )

        return Response(new_session.session_id)

# class LogOutApiView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         print(serializer())
#
#         return Response(200)
