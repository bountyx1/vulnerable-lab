from .views import index ,dynamicjs , dashboard , signup , signin , profile , reset_password , UserList
from django.urls import path ,re_path

handler404 = 'frontend.views.handler404'

urlpatterns = [
path('',index),
path('main.js',dynamicjs),
path('dashboard',dashboard),
path('signup',signup),
path('signin',signin),
path('dashboard/profile',profile),
re_path(r'dashboard/users',UserList),
path('signin/reset_password',reset_password),


]	