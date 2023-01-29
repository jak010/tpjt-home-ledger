from rest_framework.exceptions import APIException

from . import ApiCodeEnum


class AlreadyExistMember(APIException):
    status_code = 200
    default_detail = f"{ApiCodeEnum.MEMBER_DEUPLICATE.value}, 이미 등록된 멤버가 존재합니다."


class InvalidCredential(APIException):
    status_code = 400
    default_detail = "멤버 정보를 찾을 수 없음."


class InActiveMember(APIException):
    status_code = 200
    default_detail = "비활성화된 멤버"


class InvalidAccessToken(APIException):
    status_code = 400
    default_detail = "토큰이 유효하지 않음"


class DoesNotExsitEmail(APIException):
    status_code = 200
    default_detail = "존재하지 않는 이메일"
