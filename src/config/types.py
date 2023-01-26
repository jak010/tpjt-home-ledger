from __future__ import annotations

from typing import List, Union

from rest_framework.response import Response
from rest_framework.exceptions import APIException

from typing import TypeVar, Generic, Union, Final

APIResponse = Union[Response, APIException]
