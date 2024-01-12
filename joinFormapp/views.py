from django.shortcuts import render, redirect
from .forms import ApplicantForm
from joinFormapp.models import Applicant
from pageapp.models import userList
from django.utils import timezone

def show_joinForm(request):
    current_date = timezone.now().date()
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        
        if form.is_valid():
            Applicant_instance = form.save()  # 입력 데이터 저장
            
            userList.objects.create(username=Applicant_instance.name, usernum=Applicant_instance.phone_number)
      

            return redirect('joinFormapp:success_page')  # 입력 성공 후 리디렉션

    else:
        if current_date.month != 1 or current_date.day != 12:
            return render(request,'joinFormapp/arready.html')  # 조회 기간 아님
        else:
            form = ApplicantForm()

        return render(request, 'joinFormapp/application_form.html', {'form': form})

def success_page(request):
    return render(request, 'joinFormapp/success_page.html')