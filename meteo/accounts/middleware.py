class UserCookieMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        # if user and no cookie, set cookie
        if request.user.is_authenticated and not request.COOKIES.get("uuid"):
            response.set_cookie("uuid", request.user.uuid, httponly=True)
        elif not request.user.is_authenticated and request.COOKIES.get("uuid"):
            # else if if no user and cookie remove user cookie, logout
            response.delete_cookie("uuid")
        return response
