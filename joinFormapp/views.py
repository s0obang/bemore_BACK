from django.shortcuts import render, redirect
from .forms import ApplicantForm
from .models import Applicant

def show_joinForm(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 입력 데이터 저장
      

            return redirect('joinFormapp:success_page')  # 입력 성공 후 리디렉션

    else:
        form = ApplicantForm()
    
    return render(request, 'joinFormapp/application_form.html', {'form': form})

def success_page(request):
    return render(request, 'joinFormapp/success_page.html')