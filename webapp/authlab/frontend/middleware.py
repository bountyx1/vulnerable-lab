from django.http import HttpResponseForbidden

def AdminPanel(get_response):
    def middleware(request):
        if request.path == "/admin/":
             return HttpResponseForbidden()
    return middleware
