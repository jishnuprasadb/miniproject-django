

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from classroom_app.forms import LoginRegister, StudentRegister, ComplaintRegister, Notification_add
from classroom_app.models import Complaint, Notification, Student


def home(requset):
    return render(requset, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_student:
                return redirect('student_home')
        else:
            messages.info(request, 'Invalid Credentiels')
    return render(request, 'login.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def student_home(request):
    return render(request, 'student_home.html')


def student_register(request):
    login_form = LoginRegister()
    stud_form = StudentRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        stud_form = StudentRegister(request.POST)
        if login_form.is_valid() and stud_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            u = stud_form.save(commit=False)
            u.user=user
            u.save()
            messages.info(request, 'user register successful')
            return redirect('login')
    return render(request, 'student_register.html', {'login_form': login_form, 'stud_form': stud_form})


def complaint_add(request):
    form=ComplaintRegister()
    u=request.user
    if request.method=='POST':
        form=ComplaintRegister(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            messages.info(request,"complaint register successfull")
            return redirect("complaint_add")
    else:
        form=ComplaintRegister()
    return render(request,'complaint_add.html',{'form':form})

def complaint_view(request):
    dataset = Complaint.objects.all()
    print(dataset)
    context = {
        'data': dataset
    }
    return render(request,'complaint_view.html',context)




def notification(request):
    form=(Notification_add)
    u=request.user
    if request.method=='POST':
        form=Notification_add(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            messages.info(request,"notification register successfull")
            return redirect("notification")
    else:
        form=Notification_add()
    return render(request,'Notification_add.html',{'form':form})

def notification_view(request):
    dataset=Notification.objects.all()
    print(dataset)
    context={
        'data':dataset
    }
    return render(request,'notificaton_view.html',context)


def student_view(request):
    dataset=Student.objects.all()
    print(dataset)
    context={
        'data':dataset
    }
    return render(request,'student_view.html',context)


def update_view(request, id):
    obj = Student.objects.get(id=id)
    form = StudentRegister(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('student_view')
    return render(request, 'update_view.html', {'form': form})


def delete_view(request, id):
    obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('student_view')
    return render(request, 'delete_view.html')



