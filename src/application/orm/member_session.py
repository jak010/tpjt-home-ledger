from __future__ import annotations

from django.db import models

from .member import Member


class MemberSession(models.Model):
    session_id = models.UUIDField(auto_created=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    token = models.TextField()
    expire_daate = models.DateTimeField()
    iat_date = models.DateTimeField()

    class Meta:
        app_label = 'application'
        db_table = "member_session"
