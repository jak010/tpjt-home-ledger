from django.urls import path

from .views import (
    auth,
    member,
    account_book,
    account_book_history
)

app_name = "application"

urlpatterns = [

    # JWT Auth
    path('login', auth.LoginView.as_view(), name='login'),
    path('logout', auth.LogOutView.as_view(), name='logout'),

    #  Member
    path("member", member.MemberView.as_view(), name="member"),

    # Accountbook
    path("account/book", account_book.AccountBookView.as_view(), name="account_book"),
    path("account/book/<int:account_book_id>",
         account_book.AccountBookDetailView.as_view(), name="account_book_detail"),

    # AccountBookHistory
    path("account/book/<int:account_book_id>/history",
         account_book_history.AccountBookHistoryCreateView.as_view(), name="account_book_history_create"),
    path("account/book/<int:account_book_id>/history/<int:account_book_history_id>",
         account_book_history.AccountBookHistoryDetailView.as_view(), name="account_book_history_detail")

]
