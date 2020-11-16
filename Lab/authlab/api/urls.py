from django.urls import path , include
from api.views import UserViewDetail , RegistrationAPIView ,LoginAPIView , ResetPassword , UserListView
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'reset',ResetPassword,basename="token-gen")


urlpatterns = [
path('', include(router.urls)),
path('user/<int:uid>',UserViewDetail.as_view()),
path('user/signup',RegistrationAPIView.as_view()),
path('user/signin',LoginAPIView.as_view()),
path('user',UserListView.as_view()),
]	