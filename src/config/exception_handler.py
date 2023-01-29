from rest_framework.views import exception_handler


def application_exception_handler(exc,context):
    response = exception_handler(exc,context)

    if response is not None:
        response.data['status'] = response.status_code

    return response
