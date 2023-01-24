from rest_framework import serializers
from rest_framework_simplejwt.tokens import (
    RefreshToken, TokenError
)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        print(self.token)
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError as err:
            self.fail("Bad Token")
