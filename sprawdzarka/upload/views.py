from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render, redirect
from upload import models
from .forms import SendedTasksForm
from .forms import TasksListForm
from .models import SendedTasks
from .models import TaskList
from api import serializers
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .antyplagiat import *
from .xml_metric import xmlmetricf
from users.models import Account

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = serializers.StudentSerializer

@staff_member_required(login_url='login')
def task_sended_list(request):
    sended=SendedTasks.objects.all()
    return render(request,'upload/task_sended_list.html',{'sended': sended})

@login_required
def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=SendedTasksForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

@login_required
def read_file1(request, file_to_open):
    f = open(r'task/sendedtasks/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)

def task_list(request):
    sended=TaskList.objects.all
    return render(request,'upload/task_List.html',{'sended': sended})

@staff_member_required(login_url='login')
def task_List_upload(request):
    if request.method=='POST':
        form = TasksListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=TasksListForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

@login_required
def read_file2(request, file_to_open):
    f = open(r'task/tasklist/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)

@staff_member_required(login_url='login')
def plagiat(request):
    result_list = []
    file_content=""
    Lista=[]
    for file in SendedTasks.objects.all():
        Lista.append(file)
    dlug=len(Lista)
    for i in range(dlug):
        for j in range (i+1,dlug,1):
            file_content = ""
            plagiarism = ProgramFile("Bartłomiej Nowak", "434162", "15")
            file1, file2 = plagiarism.get_file(Lista[i].task.name, Lista[j].task.name)
            name_surname1, nr_index1, count_pkt1 = plagiarism.ReadReport(file1)
            name_surname2, nr_index2, count_pkt2 = plagiarism.ReadReport(file2)
            first_list, second_list = plagiarism.get_words(file1, file2)
            text_list1, text_list2 = plagiarism.get_textlist(first_list, second_list)
            if len(text_list1) != 0 and len(text_list2) != 0:
                to_check, count_of_the_same_or_similar = plagiarism.check_words(text_list1, text_list2)
                if len(text_list1) >= len(text_list2):
                    for checked in to_check:
                        result = plagiarism.check_the_similar_words(checked, text_list1)
                        count_of_the_same_or_similar += result
                    total = len(text_list1)
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                else:
                    for checked in to_check:
                        result = plagiarism.check_the_similar_words(checked, text_list2)
                        count_of_the_same_or_similar += result
                    total = len(text_list2)
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                if plagiarism_coefficient >= 30:
                    file_content += str(name_surname1)+ " " +str(nr_index1) + " całkowita ilość punktów "+ str(count_pkt1) +" "+str(xmlmetricf(Lista[i].task.name))+  " | "  +str(name_surname2) + " całkowita ilość punktów "+ str(count_pkt2) +" "+ str(nr_index2) + " "+str(xmlmetricf(Lista[j].task.name)) +" | " +"Procent podobieństwa " + str(plagiarism_coefficient)
                else:
                    file_content += str(name_surname1)+ " " +str(nr_index1) + " całkowita ilość punktów "+ str(count_pkt1) +" "+str(xmlmetricf(Lista[i].task.name))+  " | "  +str(name_surname2) + " całkowita ilość punktów "+ str(count_pkt2) +" "+ str(nr_index2) + " "+str(xmlmetricf(Lista[j].task.name)) +" | "
                    file_content +="Oba teksty mają "+ str(plagiarism_coefficient) + " procent podobnych słów. "
                    file_content +="Prace są różne! Nie stwierdzam plagiatu!!"
            else:
                file_content +="Nie można sprawdzić plagiatu dla pustych plików"
            result_list.append(file_content)
    return render(request,'upload/plagiat.html', {'result_list': result_list})



