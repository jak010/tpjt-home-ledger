from django.urls import path

from .views import (
    auth,
    member
)

app_name = "application"

urlpatterns = [

    # JWT Auth
    path('auth/token', auth.ApplicationTokenPairView.as_view(), name='token_obtain_pair'),

    #  Member
    path("member", member.MemberView.as_view(), name="member"),

]
