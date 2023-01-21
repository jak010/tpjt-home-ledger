from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class SampleTable(models.Model):
    class Meta:
        db_table = 'sample'
        app_label = "application"

    memo = models.CharField(max_length=25)
