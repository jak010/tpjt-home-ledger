from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from src.application.exceptions import member_exception
from src.application.service import member_service


class ApplicationTokenSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, kwargs):
        email = kwargs.get('email', None)
        password = kwargs.get('password', None)

        if email is None or password is None:
            raise member_exception.InvalidCredential()

        login_member = member_service.login(
            email=email,
            password=password
        )
        token = self.get_token(login_member)

        return {
            'member': {
                'email': login_member.email
            },
            'access_token': str(token.access_token),
            'refresh_token': str(token)

        }
