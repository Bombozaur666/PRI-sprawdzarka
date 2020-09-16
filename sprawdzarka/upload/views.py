from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render, redirect
from upload import models
from .forms import SendedTasksForm
from .forms import TasksListForm
from .models import SendedTasks
from .models import TaskList
from api import serializers
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.StudentSerializer

def task_sended_list(request):
    sended=SendedTasks.objects.all
    return render(request,'task_sended_list.html',{'sended': sended})

def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=SendedTasksForm()
    return render(request,'task_sended_upload.html', {'form': form})

def read_file1(request, file_to_open):
    f = open(r'task/SendedTasks/'+file_to_open, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

def task_list(request):
    sended=TaskList.objects.all
    return render(request,'task_List.html',{'sended': sended})

def task_List_upload(request):
    if request.method=='POST':
        form = TasksListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=TasksListForm()
    return render(request,'task_sended_upload.html', {'form': form})

def read_file2(request, file_to_open):
    f = open(r'task/TaskList/'+file_to_open, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
