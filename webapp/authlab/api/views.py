from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer  , RegistrationSerializer , LoginSerializer , PasswordSerializer
from .models import User , Logs
from rest_framework import status , viewsets , generics
from django.http import Http404
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import authentication
from .password_reset import UserReset
from rest_framework.decorators import action
from django.shortcuts import render

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)





class ResetPassword(viewsets.ViewSet):
	#Turning detail=True makes it like this /api/reset/pk(id we dont need)/password_reset
	@action(methods=['post'], detail=False, permission_classes=[])
	def password_reset(self,request,pk=None):
		email=request.data.get("email")
		reset = UserReset()
		response=reset.generate_token(email,request)
		if response:
			return Response('{"data":"Success"}')
		else:
			return Response('{"data":"error sending"}')

	@action(methods=['get'], detail=False, permission_classes=[])
	def token(self,request):

		token  = request.query_params["token"]
		reset = UserReset()
		response=reset.validate_token(token)
		if response["status"] == "valid":
			context = {"email":response["email"]}
			return render(request,"reset-form.html",context=context)
		else:
			return Response(response)

	@action(methods=['put'], detail=False, permission_classes=[])
	def change(self,request):
		email=request.data.get("email")
		user=User.objects.get(email=email)
		serializer=PasswordSerializer(user,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response("{'data':'success'}")
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
    	serializer = self.serializer_class(data=request.data)
    	serializer.is_valid(raise_exception=True)
    	#ipaddress = request.META['HTTP_X_FORWARDED_FOR']
    	#useragent = request.META['HTTP_USER_AGENT']
    	#user = User()
    	#user = user.__class__.objects.get(email=request.data.get("email"))
    	#logging = Logs(ip=ipaddress,useragent=useragent,)
    	#logging.save()
    	response=Response(serializer.data, status=status.HTTP_200_OK,headers={"Set-Cookie":"token="+serializer.data["token"]+";path=/ "})
    	return response




#Shortcut it must have queryset serializer_class else error you can also overwide it 
class UserListView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer




class UserViewDetail(APIView):
	permission_classes = (IsAuthenticated,)
	
	def get_user(self,uid):
		try:
			return User.objects.get(id=uid)
		except User.DoesNotExist:
			raise Http404

	def get(self,request,uid,format=None):
		user=self.get_user(uid)
		serializer=UserSerializer(user)
		return Response(serializer.data)

	def put(self,request,uid,format=None):
		user=self.get_user(uid)
		serializer=UserSerializer(user,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def delete(self,request,uid,format=None):
		user=self.get_user(uid)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

