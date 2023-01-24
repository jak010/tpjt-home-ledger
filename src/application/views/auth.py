from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from .serializers import LogoutSerializer
from .serializers.ApplicationTokenSerializer import ApplicationTokenSerializer


class LoginApiView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ApplicationTokenSerializer


class LogOutApiView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        print(serializer())

        return Response(200)
