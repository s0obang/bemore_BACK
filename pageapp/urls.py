
from django.urls import  path
from .views import *
from . import views

app_name = 'pageapp'

urlpatterns = [

 path('', views.index, name='index'),
 path('login/', views.login, name='login'),
 
]
