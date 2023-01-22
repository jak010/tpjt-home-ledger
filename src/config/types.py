from __future__ import annotations

from typing import List, Union

from rest_framework.response import Response
from rest_framework.exceptions import APIException

from typing import TypeVar, Generic, Union

AE = TypeVar('AE', bound=APIException)
R = TypeVar('R', bound=Response)

APIResponse = Union[R, Union[List[AE]]]
