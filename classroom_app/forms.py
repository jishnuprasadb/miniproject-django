from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from classroom_app.models import Student, Login, Complaint,Notification


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class StudentRegister(forms.ModelForm):
    class Meta:
        model=Student
        fields = ('name', 'email', 'roll_no', 'college_name', 'phone_number')


class DateInput(forms.DateInput):
        input_type='date'


class ComplaintRegister(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model=Complaint
        fields=('subject','complaint','date',)



class Notification_add(forms.ModelForm):
    class Meta:
        model=Notification
        fields=('subject','notification')



