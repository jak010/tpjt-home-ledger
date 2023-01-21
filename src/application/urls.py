from django.urls import path

from .views import member

app_name = "application"

urlpatterns = [

    #  Member
    path("member", member.MemberView.as_view(), name="member")

]
