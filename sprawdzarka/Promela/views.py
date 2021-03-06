from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import *
from .promeli_filechcker import *
from django.contrib import messages
import os

def filename(value):
    return os.path.basename(value.file.name)

@staff_member_required(login_url='login')
def change_points_promela_direct(request,id_in_url):
    if request.method=='POST':
        form = TransformersForm(request.POST)
        if form.is_valid():
            object=StudentTask.objects.get(id=id_in_url)
            object.points=form.cleaned_data['NewPoints']
            object.save()
            return redirect('promela-sended-list' )
    else:
        form=TransformersForm()
    return render(request,'upload/transformers.html', {'form': form})

@staff_member_required(login_url='login')
def task_promela_upload_teacher(request):
    if request.method=='POST':
        form = TeacherTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.tname = request.user.username
            form.save()
    else:
        form=TeacherTaskForm()
    return render(request,'Promela/task_promela_upload.html', {'form': form})


@login_required
def task_promela_upload(request):
    if request.method=='POST':
        form = StudentTaskForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            if StudentTask.objects.filter(snumber = request.user.snumber, task_id = object.task_id).exists():
                messages.warning(request,"Nie można dodać 2 razy tego samego zadania.")
            else:
                object.snumber = request.user.snumber
                object.group_id = request.user.group_id               
                object.save()

    else:
        form= StudentTaskForm()
    return render(request, 'upload/task_sended_upload.html', {'form': form})

@staff_member_required(login_url='login')
def task_Promela_student_sended_list(request):
    promela_funck()
    sended=StudentTask.objects.all()
    for task in sended:
        task.task_file.name = (os.path.basename(task.task_file.name))
        task.output_file.name = (os.path.basename(task.output_file.name))
    return render(request,'Promela/task_Promela_sended_list.html',{'sended': sended})

@login_required
def task_list_promela(request):
    sended=TeacherTask.objects.all()
    for task in sended:
        task.file.name = (os.path.basename(task.file.name))
    return render(request,'Promela/task_List_promela.html',{'sended': sended})

@login_required
def read_file_promela__task_list(request, file_to_open):
    f = open(r'task/promela/teacher_ltl/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)


@login_required
def read_file_Promela_task_student(request, file_to_open):
    f = open(r'task/promela/student_files/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)