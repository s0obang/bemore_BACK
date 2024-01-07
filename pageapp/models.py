from django.db import models

# Create your models here.
#passList 합격db, userList 회원 db 

class passList(models.Model):
    username = models.CharField(max_length= 25,unique = False )
    usernum  = models.CharField(max_length= 25,unique = True)


class userList(models.Model):
    username = models.CharField(max_length= 25,unique = False)
    usernum  = models.CharField(max_length= 25,unique = True)


