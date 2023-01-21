from django.urls import path

from .views import member

urlpatterns = [

    #  Member
    path("member", member.MemberView.as_view())

]
