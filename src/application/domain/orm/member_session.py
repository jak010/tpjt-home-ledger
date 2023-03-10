from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models

Member = get_user_model()


class MemberSession(models.Model):
    session_id = models.UUIDField(auto_created=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    token = models.TextField()
    expire_time = models.PositiveIntegerField()
    iat_time = models.PositiveIntegerField()

    objects = models.Manager()

    class Meta:
        app_label = 'application'
        db_table = "member_session"
