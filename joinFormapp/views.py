from django.shortcuts import render, redirect
from .forms import ApplicantForm
from .models import Applicant

from django.shortcuts import render, redirect
from .models import Applicant
from django.contrib import messages 

def show_joinForm(request):
    if request.method == 'POST':
        # POST 요청일 때, 지원서 데이터를 저장합니다.
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        introduction = request.POST.get('introduction')
        motivation = request.POST.get('motivation')
        activity_attachment = request.FILES.get('activity_attachment')
        github_or_tistory = request.POST.get('github_or_tistory')

        # 지원서 모델에 데이터 저장
        applicant = Applicant(
            name=name,
            phone_number=phone_number,
            introduction=introduction,
            motivation=motivation,
            activity_attachment=activity_attachment,
            github_or_tistory=github_or_tistory
        )
        applicant.save()

        messages.success(request, '지원서가 성공적으로 제출되었습니다. 감사합니다!')

        # 저장이 완료되면 어떤 페이지로 redirect할지 정의합니다.
        return redirect('joinFormapp:show_joinForm')

    else:
        # GET 요청일 때, 지원서 입력 폼을 보여줍니다.
        return render(request, 'joinFormapp/application_form.html')