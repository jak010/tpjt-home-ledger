from __future__ import annotations

from django.db import models

from .member import Member


class MemberSession(models.Model):
    session_id = models.UUIDField(auto_created=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    token = models.TextField()
    expire_time = models.PositiveIntegerField()
    iat_time = models.PositiveIntegerField()

    objects = models.Manager()

    class Meta:
        app_label = 'application'
        db_table = "member_session"
