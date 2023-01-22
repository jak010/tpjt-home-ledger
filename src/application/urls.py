from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    auth,
    member
)

app_name = "application"

urlpatterns = [

    # JWT Auth

    path('token', auth.ApplicationTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    #  Member
    path("member", member.MemberView.as_view(), name="member")

]
