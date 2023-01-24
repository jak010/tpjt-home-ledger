from django.urls import path

from .views import (
    auth,
    member
)

app_name = "application"

urlpatterns = [

    # JWT Auth
    path('login', auth.LoginView.as_view(), name='login'),
    path('logout', auth.LogOutView.as_view(), name='logout'),

    #  Member
    path("member", member.MemberView.as_view(), name="member"),

]
