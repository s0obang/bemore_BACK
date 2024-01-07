from django.db import models

# Create your models here. 
class Applicant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    introduction = models.TextField()
    motivation = models.TextField()
    activity_attachment = models.FileField(upload_to='activity_attachments/')
    github_or_tistory = models.URLField(blank=True)

    # 게시글의 제목을 name으로 설정
    def __str__(self):
        return self.name
