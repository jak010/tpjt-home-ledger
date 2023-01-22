from datetime import datetime

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from ..exceptions import member_exception
from ..libs import utils
from ..orm.member import Member


class ApplicationTokenSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, kwargs):
        email = kwargs.get('email', None)
        password = kwargs.get('password', None)

        if email is None or password is None:
            raise member_exception.InvalidCredential()

        check_member = self.check(email, password)
        token = self.get_token(check_member)

        return {
            'member': {
                'email': check_member.email
            },
            'access_token': str(token.access_token),
            'refresh_token': str(token)

        }

    def check(self, email: str, password: str):
        try:
            member = Member.objects.get(email=email)
        except Member.DoesNotExist as e:
            raise member_exception.InvalidCredential()

        if not utils.check_password(password, member.password.encode()):
            raise member_exception.InvalidCredential()

        if member.is_active != 1:
            raise member_exception.InActiveMember()

        member.last_login = datetime.now()
        member.save()
        return member


class ApplicationTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ApplicationTokenSerializer
