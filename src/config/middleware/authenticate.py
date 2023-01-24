class TokenAuthenticateMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화

    def __call__(self, request):
        # 뷰가 호출되기 전에 실행될 코드들

        response = self.get_response(request)

        # 뷰가 호출된 뒤에 실행될 코드들

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("JWT Authenticate Process Logic")
