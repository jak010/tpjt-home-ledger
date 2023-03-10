from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models

Member = get_user_model()


class AccountBook(models.Model):
    reference_id = models.AutoField(primary_key=True)

    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "accountbook"


class AccountBookHistory(models.Model):
    reference_id = models.AutoField(primary_key=True)
    account_book = models.ForeignKey(AccountBook, related_name='history',
                                     on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=1)

    memo = models.CharField(max_length=128)
    amount = models.PositiveIntegerField()

    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "accountbook_history"
