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
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .antyplagiat import *
from .xml_metric import xmlmetricf
from .Antyplagiat_Extended import *
from .RabinKarp import *

class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
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
    return render(request,'upload/wyswietlanie.html',{'result': result})

@staff_member_required(login_url='login')
def plagiat(request):
    result_list = []
    file_content = ""
    second_content = ""
    third_content = ""
    fourth_content = "//////////////////////////////////"
    Lista = []
    for file in SendedTasks.objects.all():
        Lista.append(file)
    temp = []
    for i in range(len(Lista)):
        temp.append(Lista[i].task.name)
    already_checked_files = []
    files_and_enlargement = get_file(temp)
    for first_file in files_and_enlargement:
        already_checked_files.append(first_file)
        for second_file in files_and_enlargement:
            if first_file != second_file and second_file not in already_checked_files:
                name_of_first_file = []
                name_of_second_file = []
                i = len(first_file) - 1
                while(first_file[i] != '/'):
                    name_of_first_file.append(first_file[i])
                    i = i - 1
                name_of_first_file.reverse()
                name_of_first_file = ''.join(str(i) for i in name_of_first_file)
                #print(name_of_first_file)
                j = len(second_file) - 1
                while second_file[j] != '/':
                    name_of_second_file.append(second_file[j])
                    j = j - 1
                name_of_second_file.reverse()
                name_of_second_file = ''.join(str(j) for j in name_of_second_file)
                file_content += str(name_of_first_file) + " i " + str(name_of_second_file) + ": "
                if (files_and_enlargement[first_file] == ".txt" and files_and_enlargement[second_file] == '.txt') or (files_and_enlargement[first_file] == ".txt" and files_and_enlargement[second_file] == ".xml") or (files_and_enlargement[first_file] == ".xml" and files_and_enlargement[second_file] == ".txt") or (files_and_enlargement[first_file] == ".xml" and files_and_enlargement[second_file] == ".xml"):
                    file1 = open(first_file, 'r', encoding="utf-8", errors="ignore")
                    file2 = open(second_file, 'r', encoding="utf-8", errors="ignore")
                    report = ProgramFile("Bartlomiej Nowak", "434589", "15")
                    name_surname1, nr_index1, count_pkt1 = report.ReadMetric(file1)
                    name_surname2, nr_index2, count_pkt2 = report.ReadMetric(file2)
                    words1, words2 = report.get_words(file1, file2)
                    text1, text2 = report.get_textlist(words1, words2)
                    not_repeat1, not_repeat2 = report.remove_repeat(text1, text2)
                    similars = []
                    txt = ""
                    q = 101 #Liczba pierwsza
                    if len(not_repeat1) > 0 and len(not_repeat2) > 0:
                        if len(not_repeat1) >= len(not_repeat2):
                            txt = " ".join([str(i) for i in not_repeat1])
                            for word in not_repeat2:
                                indexes = []
                                indexes = report.Rabin_Karp_algorithm(word, txt, q)
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
                                indexes = report.Rabin_Karp_algorithm(word, txt, q)
                                if len(indexes) > 0:
                                    if word not in similars:
                                        similars.append(word)
                                    else:
                                        continue
                            total = len(not_repeat2)
                            count_of_the_same_or_similar = len(similars)
                            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
                        if name_surname1 != name_surname2:
                            if plagiarism_coefficient >= 30 and plagiarism_coefficient <= 100:
                                    second_content += str(plagiarism_coefficient) + "% podobieństwa. "
                                    second_content += "PLAGIAT!!! "
                                    if (name_surname1 == "-" or nr_index1 == '-' or count_pkt1 == '-') and (name_surname2 == '-' or nr_index2 == '-' or count_pkt2 == '-'):
                                        third_content += "Nie można zweryfikować wszystkich danych obu studentów w plikach ", + str(first_file) + " i " + str(second_file)
                                    elif name_surname1 == '-' or nr_index1 == '-' or count_pkt1 == '-':
                                        third_content += "Nie można zweryfikować wszystkich danych studenta w pliku " + str(first_file) + " "
                                        third_content += "Osoba która dopuściła się plagiatu to: " + str(name_surname2) + " o numerze indeksu " + str(nr_index2)
                                    elif name_surname2 == '-' or nr_index2 == '-' or count_pkt2 == '-':
                                        third_content += "Osoba która dopuściła się plagiatu to: " + str(name_surname1) + " o numerze indeksu " + str(nr_index1) + " "
                                        third_content += "Nie można zweryfikować wszystkich danych studenta w pliku " + str(second_file)
                                    else:
                                        third_content += "Osoby, które dopuściły się plagiatu to: " + str(name_surname1) + " o numerze indeksu " + str(nr_index1) + " oraz " + str(name_surname2) + " o numerze indeksu " + str(nr_index2)
                            else:
                                second_content += str(plagiarism_coefficient) + "% podobieństwa. "
                                second_content += "NIE MA PLAGIATU!!"
                        else:
                            third_content += "Prace należą do tego samego studenta."
                    else:
                        third_content += "Nie można sprawdzić plagiatu dla plików pustych lub bez rozwiązania"
                else:
                    continue
            else:
                continue
            result_list.append(file_content)
            result_list.append(second_content)
            result_list.append(third_content)
            result_list.append(fourth_content)
            file_content = ""
            second_content = ""
            third_content = ""
    return render(request, 'upload/plagiat.html', {'result_list': result_list})






