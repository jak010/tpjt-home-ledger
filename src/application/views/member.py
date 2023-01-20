from __future__ import annotations

from rest_framework.views import APIView
from rest_framework.response import Response


class MemberView(APIView):

    def get(self, *args, **kwags):
        return Response()
