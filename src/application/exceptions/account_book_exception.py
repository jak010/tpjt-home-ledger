from rest_framework.exceptions import APIException


class DoesNotExsitAccountBook(APIException):
    status_code = 400
    default_detail = "가계부 정보를 찾을 수 없음"
