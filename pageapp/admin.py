from django.contrib import admin
# Register your models here.
# 어드민에 모델 추가 설정
from pageapp.models import passList
from pageapp.models import userList

admin.site.register(passList)
admin.site.register(userList)

# Register your models here.
