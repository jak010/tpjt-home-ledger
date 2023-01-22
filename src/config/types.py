from __future__ import annotations

from rest_framework.response import Response
from rest_framework.exceptions import APIException

from typing import TypeVar, Generic, Union

A = TypeVar('A', bound=APIException)
R = TypeVar('R', bound=Response)

APIResponse = Union[A, R]
