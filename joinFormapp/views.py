from django.shortcuts import render, redirect
from joinFormapp.models import Applicant
from pageapp.models import userList
from django.utils import timezone
from django.contrib import messages

def show_joinForm(request):
    current_date = timezone.now().date()
    # POST 요청일 때, 지원서 데이터를 저장합니다.
    if request.method == 'POST':
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
        
        userList.objects.create(username=applicant.name, usernum=applicant.phone_number)
        messages.success(request, '지원서가 성공적으로 제출되었습니다. 감사합니다!')
        # 저장이 완료되면 어떤 페이지로 redirect할지 정의합니다.
        return redirect('joinFormapp:show_joinForm')
    else:
        if current_date.month != 1 or current_date.day != 12:
            return render(request, 'joinFormapp/arready.html')  # 조회 기간 아님
        else:
            # GET 요청일 때, 지원서 입력 폼을 보여줍니다.
            return render(request, 'joinFormapp/application_form.html')
