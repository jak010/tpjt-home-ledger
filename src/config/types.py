from __future__ import annotations

from typing import Union, TypeVar

from django.db import models
from django.contrib.auth import get_user_model

from rest_framework.exceptions import APIException
from rest_framework.response import Response

APIResponse = Union[Response, APIException]

DjangoModel = TypeVar('DjangoModel', bound=models.Model)
