from __future__ import annotations

from typing import Union

from rest_framework.exceptions import APIException
from rest_framework.response import Response

APIResponse = Union[Response,APIException]
