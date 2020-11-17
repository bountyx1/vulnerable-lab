from django.http import HttpResponse
import re
class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        result= re.search("^/admin.*",request.path)
        # X-Forwaded bypass + python obj format + xss 
        if result != None and "127.0.0.1" not in ip:
            msg = "Request to {obj.path} is not allowed from "+ip
            return HttpResponse(msg.format(obj=request))
        else:
            return self.get_response(request)
        return self.get_response(request)
