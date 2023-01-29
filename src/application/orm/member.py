from __future__ import annotations

from django.contrib.auth.models import (
    AbstractBaseUser as _AbstractBaseUser, BaseUserManager
)

from config.types import DjangoModel
from django.db import models, IntegrityError

from ..exceptions import member_exception
from ..libs import utils


class Member(_AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=72)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    manager = BaseUserManager()

    class Meta:
        db_table = "member"
        app_label = "application"
