from django.urls import path

from .views import (
    auth,
    member,
    accountbook,
    accountbook_history
)

app_name = "application"

urlpatterns = [

    # JWT Auth
    path('login',auth.LoginView.as_view(),name='login'),
    path('logout',auth.LogOutView.as_view(),name='logout'),

    #  Member
    path("member",member.MemberView.as_view(),name="member"),

    # Accountbook
    path("accountbooks",accountbook.AccountsBookView.as_view(),name="accountbooks"),
    path("accountbooks/<int:accountbook_id>",
         accountbook.AccountBookDetailView.as_view(),name="accountbooks_detail"),

    # AccountBookHistory
    path("accountbooks/<int:accountbook_id>/history",
         accountbook_history.AccountBookHistoryCreateView.as_view(),name="accountbooks_history_create"),
    path("accountbooks/<int:accountbook_id>/history/<int:accountbook_history_id>",
         accountbook_history.AccountBookHistoryDetailView.as_view(),name="accountbook_history_detail"),
    path("accountbooks/<int:accountbook_id>/history/<int:accountbook_history_id>/restore",
         accountbook_history.AccountBookHistoryRestoreView.as_view(),name="accountbook_history_restore")
]
