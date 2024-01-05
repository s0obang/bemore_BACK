from django.contrib import admin
# Applicant Model을 불러옵니다
from .models import Applicant

# 관리자(admin)가 Applicant에 접근 가능
admin.site.register(Applicant)