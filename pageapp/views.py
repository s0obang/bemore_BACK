from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth
from .models import userList
from .models import passList
from django.http import HttpResponse
from django.utils import timezone
from django import forms
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def login(request):
    current_date = timezone.now().date()
    if request.method ==  'POST': #로그인 요청시 로그인
        username = request.POST.get('username',None)
        usernum = request.POST.get('usernum',None)
        error = {}

        
       
        try:
            user = userList.objects.get(username=username, usernum=usernum)
            passuser = passList.objects.get(usernum = usernum,username=username)
        
            
        except userList.DoesNotExist:
            error['error'] = '해당하는 사용자가 없습니다.'
            return render(request, 'main/login.html', error)
        
        except passList.DoesNotExist:
            return render(request,'main/result2.html')
        
        return render(request,'main/result.html')
    
    else:
         if current_date.month != 1 or current_date.day != 7:
            return render(request,'main/arready.html')  
         else:
            return render(request,'main/login.html') #get 요청시 login html 띄움


