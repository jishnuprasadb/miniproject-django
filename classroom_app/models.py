from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)


class Student(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    roll_no = models.IntegerField()
    college_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Complaint(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    subject=models.CharField(max_length=100)
    complaint=models.TextField()
    date=models.DateField()
    reply=models.TextField(null=True,blank=True)

class Notification(models.Model):
    subject = models.CharField(max_length=100)
    notification = models.TextField()

