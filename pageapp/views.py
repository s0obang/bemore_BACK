from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import auth
from .models import userList
from .models import passList
from django.http import HttpResponse
from django.utils import timezone
from django import forms
# Create your views here.

# 메인화면
def index(request):
    return render(request, 'main/index.html')
# 동아리 소개
def intro(request):
    return render(request, 'bemore_intro/introduce.html')
# 동아리 활동
def act(request):
    return render(request, 'bemore_intro/activity.html')
# 합격자 조회
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
            return render(request,'result/fail.html') # 불합격
        
        return render(request,'result/pass.html') # 합격
    
    else:
         if current_date.month != 1 or current_date.day != 12:
            return render(request,'main/arready.html')  # 조회 기간 아님
         else:
            return render(request,'main/login.html') #get 요청시 login html 띄움


