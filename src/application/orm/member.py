from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Member(AbstractBaseUser):
    class Meta:
        db_table = 'member'
        app_label = 'application'

    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=60)

    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(blank=True, null=True)

    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()
