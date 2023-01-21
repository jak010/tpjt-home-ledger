from rest_framework.exceptions import APIException

from . import ApiCodeEnum


class AlreadyExistMember(APIException):
    status_code = 200
    default_detail = f"{ApiCodeEnum.MEMBER_DEUPLICATE.value}, 이미 등록된 멤버가 존재합니다."
