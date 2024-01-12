from django.urls import path
from .views import show_joinForm

app_name = 'joinFormapp'


urlpatterns = [
    path('show_joinForm/', show_joinForm, name='show_joinForm'),
    #path('success_page/', success_page, name='success_page'),
 #   path('', show_joinForm),
    # 다른 URL 패턴들을 추가할 수 있음
]