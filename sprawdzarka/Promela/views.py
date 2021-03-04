from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import *
from .promeli_filechcker import *
from django.contrib import messages

@staff_member_required(login_url='login')
def task_promela_upload_list(request):
    if request.method=='POST':
        form = TeacherTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.tname = request.user.username
            form.save()
    else:
        form=TeacherTaskForm()
    return render(request,'upload/task_promela_upload.html', {'form': form})

@staff_member_required(login_url='login')
def task_Promela_student_sended_list(request):
    promela_funck()
    sended=Promela2.objects.all()
    return render(request,'upload/task_Promela_sended_list.html',{'sended': sended})

@login_required
def task_promela_upload(request):
    if request.method=='POST':
        form = StudentTaskForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            if Promela.objects.filter(snumber = request.user.snumber, taskid = object.taskid).exists():
                messages.warning(request,"Nie można dodać 2 razy tego samego zadania.")
            else:
                object.snumber = request.user.snumber
                object.taskcopy = form.task
                object.save()
    else:
        form= StudentTaskForm()
    return render(request, 'upload/task_sended_upload.html', {'form': form})

@login_required
def read_file_promela__task_list(request, file_to_open):
    f = open(r'task/PromelaList//'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)

def task_list_promela(request):
    sended=TaskListPromela.objects.all
    return render(request,'upload/task_List_promela.html',{'sended': sended})

@login_required
def read_file_Promela_task_student(request, file_to_open):
    f = open(r'task/Promela/Studentstask/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)@login_required

def read_file_Promela_output(request, file_to_open):
    f = open(r'task/Promela/Studentoutput/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)