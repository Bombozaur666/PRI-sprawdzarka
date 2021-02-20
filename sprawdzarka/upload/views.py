from rest_framework import viewsets
from django.shortcuts import render
from .forms import *
from api import serializers
from .RabinKarp import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import SendedTasks,Plagiat
from users.models import Account
from django.contrib import messages
from .promeli_filechcker import *
from django.core.files.base import ContentFile

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = serializers.StudentSerializer


@staff_member_required(login_url='login')
def task_sended_list(request):
    sended=SendedTasks.objects.filter(max_point="0")
    for x in sended:
        listapkt, punkty  = return_points(x.task.name)
        sended.update(max_point=punkty, point=listapkt)
    sended2 = SendedTasks.objects.all()
    return render(request,'upload/task_sended_list.html',{'sended': sended2})

@staff_member_required(login_url='login')
def task_Promela_student_sended_list(request):
    promela_funck()
    sended=Promela2.objects.all()
    return render(request,'upload/task_Promela_sended_list.html',{'sended': sended})

@login_required
def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            if SendedTasks.objects.filter(snumber = request.user.snumber, taskid = object.taskid).exists():
                messages.warning(request,"Nie można dodać 2 razy tego samego zadania.")
            else:
                object.snumber = request.user.snumber
                object.save()
    else:
        form=SendedTasksForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

def task_sended_promela_upload(request):
    if request.method=='POST':
        form = SendedPromelaTasksForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            if Promela.objects.filter(snumber = request.user.snumber, taskid = object.taskid).exists():
                messages.warning(request,"Nie można dodać 2 razy tego samego zadania.")
            else:
                object.snumber = request.user.snumber
                object.taskcopy = object.task
                object.save()




    else:
        form= SendedPromelaTasksForm()
    return render(request, 'upload/task_sended_upload.html', {'form': form})

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

def task_list_choose(request):
    return render(request,'upload/task_list_choose.html')

def task_upload_choose(request):
    return render(request,'upload/task_upload_choose.html')

def task_sended_choose(request):
    return render(request,'upload/task_sended_choose.html')

def task_list_promela(request):
    sended=TaskListPromela.objects.all
    return render(request,'upload/task_List_promela.html',{'sended': sended})

@staff_member_required(login_url='login')
def task_List_upload(request):
    if request.method=='POST':
        form = TasksListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.tname = request.user.username
            form.save()
    else:
        form=TasksListForm()
    return render(request,'upload/task_sended_upload.html', {'form': form})

@staff_member_required(login_url='login')
def task_promela_upload(request):
    if request.method=='POST':
        form = TaskListPromelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.tname = request.user.username
            form.save()
    else:
        form=TaskListPromelaForm()
    return render(request,'upload/task_promela_upload.html', {'form': form})

@login_required
def read_file2(request, file_to_open):
    f = open(r'task/tasklist/'+file_to_open, encoding="utf-8")
    result = []
    for line in f:
        result.append(line)
    f.close()
    return render(request,'upload/wyswietlanie.html',{'result': result},)

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


@staff_member_required(login_url='login')
def plagiat(request):
    files_to_check = [str(elem) for elem in list(SendedTasks.objects.filter(has_been_tested=False).values_list('task', flat=True))]
    all_files = [str(elem) for elem in list(SendedTasks.objects.all().values_list('task', flat=True))]
    for first_file in files_to_check:
        for second_file in all_files:
            if second_file == first_file:
                continue
            file1 = open(first_file, 'r', encoding="utf-8", errors="ignore")
            file2 = open(second_file, 'r', encoding="utf-8", errors="ignore")                
            name_surname1, nr_index1, count_pkt1 = ReadMetric(file1)
            name_surname2, nr_index2, count_pkt2 = ReadMetric(file2)
            words1, words2 = get_words(file1, file2)
            text1, text2 = get_textlist(words1, words2)                    
            not_repeat1, not_repeat2 = remove_repeat(text1, text2)
            similars = []
            txt = ""
            q = 101  # Liczba pierwsza
            if len(not_repeat1) > 0 and len(not_repeat2) > 0:
                if len(not_repeat1) >= len(not_repeat2):
                    txt = " ".join([str(i) for i in not_repeat1])
                    for word in not_repeat2:
                        indexes = []                                
                        indexes = Rabin_Karp_algorithm(word, txt, q)
                        if len(indexes) > 0:
                            if word not in similars:
                                similars.append(word)
                            else:
                                continue
                    total = len(not_repeat1)
                    count_of_the_same_or_similar = len(similars)                            
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                else:
                    txt = " ".join([str(i) for i in not_repeat2])
                    for word in not_repeat1:
                        indexes = []
                        indexes = Rabin_Karp_algorithm(word, txt, q)
                        if len(indexes) > 0:
                            if word not in similars:
                                similars.append(word)
                            else:
                                continue
                    total = len(not_repeat2)
                    count_of_the_same_or_similar = len(similars)
                    plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
            snum1=[str(elem) for elem in list(SendedTasks.objects.filter(task = first_file).values_list('snumber', flat=True))]
            snum2 = [str(elem) for elem in list(SendedTasks.objects.filter(task = second_file).values_list('snumber', flat=True))]
            plagiat = Plagiat()
            plagiat.snumber1= snum1[0]
            plagiat.snumber2=snum2[0]
            plagiat.name1= first_file.lstrip('task/sendedtasks/')
            plagiat.name2= second_file.lstrip('task/sendedtasks/')
            plagiat.plagiat=plagiarism_coefficient
            plagiat.save()
        task = SendedTasks.objects.filter(task = first_file)
        task.update(has_been_tested = True)
    
    plagiaty = Plagiat.objects.all()
    
    return render(request, 'upload/plagiat.html', {'plagiaty':plagiaty})