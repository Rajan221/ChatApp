from importlib.resources import path
from django.urls import path, include,re_path

from . import views


#URl conf
urlpatterns =[
    path('', views.signUp, name="signup"),
    path('login/', views.login, name="login"),
   

]