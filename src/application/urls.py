from django.urls import path

from rest_framework_simplejwt.views import TokenBlacklistView

from .views import (
    auth,
    member
)

app_name = "application"

urlpatterns = [

    # JWT Auth
    path('login', auth.LoginApiView.as_view(), name='token_obtain_pair'),
    # path('logout', auth.LogOutApiView.as_view(), name='token_blacklist'),

    #  Member
    path("member", member.MemberView.as_view(), name="member"),

]
