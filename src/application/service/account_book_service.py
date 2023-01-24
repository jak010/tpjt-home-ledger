from __future__ import annotations

from ..orm.member import Member
from ..orm.account_book import AccountBook, AccountBookHistory

from ..exceptions import account_book_exception


def create_account_book(name: str, description: str, member: Member) -> AccountBook:
    """ 가계부 생성하기 """
    new_account_book = AccountBook.objects.create(
        name=name,
        description=description,
        author=member
    )

    return new_account_book


def get_account_book_with_pk(reference_id: int) -> AccountBook:
    try:
        account_book = AccountBook.objects.get(
            reference_id=reference_id
        )
    except AccountBook.DoesNotExist as e:
        raise account_book_exception.DoesNotExsitAccountBook()

    return account_book


def create_account_book_history(
        amount: str,
        memo: str,
        account_book: AccountBook) -> AccountBookHistory:
    new_account_book_history = AccountBookHistory.objects.create(
        amount=amount,
        memo=memo,
        account_book=account_book
    )

    return new_account_book_history
