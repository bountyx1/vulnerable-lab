from django.shortcuts import render , redirect
from api.models import User
from api.serializers import UserSerializer
from .backend import Authandler

# Create your views here.

def index(request):
	response = render(request,'index.html')
	return response

def signup(request):
	response = render(request,'signup.html')
	return response

def signin(request):
	response = render(request,'signin.html')
	return response

def reset_password(request):
	response = render(request,'password-reset.html')
	return response

def dashboard(request):
	auth = Authandler()
	token = request.COOKIES.get("token")
	if token != None:
		user = auth.validate(token)
		if user != None:
			user = User.objects.get(username=user)
			print(user.is_staff)
			context = {"is_staff":user.is_staff}
			response = render(request,'base-dashboard.html',context=context)
			return response
		else:
			return redirect("/signin")
	else:
		return redirect("/signin")


def UserList(request):
	auth = Authandler()
	token = request.COOKIES.get("token")
	if token != None:
		user = auth.validate(token)
		if user != None:
			user = User.objects.get(username=user)
			print(user.is_staff)
			context = {"is_staff":user.is_staff}
			response = render(request,'users.html',context=context)
			return response
		else:
			return redirect("/signin")
	else:
		return redirect("/signin")
		


def handler404(request ,*args, **kwargs):
	context={"token":"google.com"}
	response = render(request,'404.html',context=context,status_code=400)
	return response

# Dynamic js writing token
def dynamicjs(request):
	auth = Authandler()
	token = request.COOKIES.get("token")
	if token != None:
		user = auth.validate(token)
		if user != None:
			user = User.objects.get(username=user)
			serializer=UserSerializer(user)
			context= {"user":serializer.data,"token":token,"host":request.META['HTTP_HOST']}
			return render(request,'main.js',context=context,content_type="application/javascript")
		else:
			return render(request,'main.js',content_type="application/javascript")
	else:
		return render(request,'main.js',content_type="application/javascript")


def profile(request):
	auth = Authandler()
	token = request.COOKIES.get("token")
	if token != None:
		user = auth.validate(token)
		if user != None:
			user=User.objects.get(username=user)
			context = {"email":user.email,"username":user.username,"id":user.id,"is_staff":user.is_staff}
			response = render(request,'profile.html',context=context)
			return response
		else:
			return redirect("/signin")
	else:
		return redirect("/signin")