from __future__ import annotations

from ..orm.member import Member
from ..orm.accountbook import AccountBook, AccountBookHistory

from ..exceptions import accountbook_exception

from ..libs.define import AccountHistoryStatus


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
        raise accountbook_exception.DoesNotExsitAccountBook()

    return account_book


def get_account_books(member: Member):
    account_books = AccountBook.objects.filter(author=member)

    data = dict(
        summary=dict(
            count=len(account_books)
        ),
        items=[{
            'reference_id': account_book.reference_id,
            'name': account_book.name,
            'description': account_book.description,
            'date_of_create': account_book.date_of_create,  # TODO: KST로 시간대 변경 필요함
            'date_of_update': account_book.date_of_update
        } for account_book in account_books]
    )

    return data


def get_account_book_with_history(accountbook_id: int):
    # TODO: join 시키는 방법이 있을 듯 하다.
    try:
        account_book = AccountBook.objects.get(reference_id=accountbook_id)
    except AccountBook.DoesNotExist as e:
        raise accountbook_exception.DoesNotExsitAccountBook()

    account_book_history = AccountBookHistory.objects.filter(
        account_book_id=account_book.reference_id,
        is_active=1
    ).all()

    data = dict(
        account_book=dict(
            reference_id=account_book.reference_id,
            name=account_book.name,
            description=account_book.description,
            date_of_create=account_book.date_of_create,
            date_of_update=account_book.date_of_update,
        ),
        historys=[{
            'reference_id': history.reference_id,
            'amount': history.amount,
            'memo': history.memo,
            "date_of_create": history.date_of_create,
            "date_of_update": history.date_of_update,
        } for history in account_book_history]
    )

    return data


def create_account_book_history(
        amount: str,
        memo: str,
        account_book: AccountBook) -> AccountBookHistory:
    """ 가계부 내역 생성하기 """
    new_account_book_history = AccountBookHistory.objects.create(
        amount=amount,
        memo=memo,
        account_book=account_book
    )

    return new_account_book_history


def get_acoount_book_history(reference_id: int) -> AccountBookHistory:
    """ 가계부 내역 찾기 """
    try:
        account_book_history = AccountBookHistory.objects.get(
            reference_id=reference_id
        )
    except AccountBookHistory.DoesNotExist:
        raise accountbook_exception.DoesNotExsitAccountHistoryBook()

    if account_book_history.is_active == AccountHistoryStatus.Inactive.value:
        raise accountbook_exception.InActivedAccountbookHistory()

    return account_book_history


def get_account_book_history_without_status(reference_id: int) -> AccountBookHistory:
    """ 가계부 내역의 상태 상관없이 가져오기 """
    try:
        account_book_history = AccountBookHistory.objects.get(
            reference_id=reference_id
        )
    except AccountBookHistory.DoesNotExist:
        raise accountbook_exception.DoesNotExsitAccountHistoryBook()
    return account_book_history


def update_account_book_history(account_book_history: AccountBookHistory, amount: int, memo: str):
    account_book_history.amount = amount
    account_book_history.memo = memo
    account_book_history.save()
