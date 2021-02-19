from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import return_points
from .forms import SendedTasksForm
from .forms import TasksListForm
from api import serializers
from .RabinKarp import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import SendedTasks,Plagiat
from users.models import Account


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
    files_to_check = [str(elem) for elem in list(SendedTasks.objects.filter(has_been_tested = False).values_list('task', flat=True))]
    all_files = [str(elem) for elem in list(SendedTasks.objects.all().values_list('task', flat=True))]
    for first_file in files_to_check:
        for second_file in all_files:
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
                    plagiaty = Plagiat()
                    plagiaty.snumber1= snum1[0]
                    plagiaty.snumber2=snum2[0]
                    plagiaty.name1= first_file
                    plagiaty.name2= second_file
                    plagiaty.plagiat=(str(plagiarism_coefficient) + "%")
                    plagiaty.save()
        task = SendedTasks.objects.filter(task = first_file)
        task.update(has_been_tested = True)
    return(render(request, 'upload/plagiat.html'))