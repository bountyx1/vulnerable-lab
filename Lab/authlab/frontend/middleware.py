from django.http import HttpResponseForbidden

def admi:
	def process_request(self,request):
		if "/admin/" in request.path:
			request.META['HTTP_X_FORWARDED_FOR']
			if request.META['HTTP_X_FORWARDED_FOR'] != '127.0.0.1':
				return HttpResponseForbidden()