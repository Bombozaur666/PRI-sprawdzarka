from django.shortcuts import render, redirect
from .models import *
from upload import models as upload_models
from django.contrib.auth.decorators import login_required
from .form import AddQuestionForm,AddAnswerForm

@login_required
def all(request):
    all_questions = Question.objects.all()
    return render(request, 'forum/all_questions.html', {'all':all_questions})
@login_required
def question(request, id):
    this_id = id
    this_question = Question.objects.get(id = this_id)
    no_answer = ''
    teacher_answers = []
    answers = []
    check = False
    if Answer.objects.filter(question_id = this_id).exists():
        answers = Answer.objects.filter(question_id = this_id, has_teacher_answered = False)
        if Answer.objects.filter(question_id = this_id, has_teacher_answered = True).exists():
            teacher_answers = Answer.objects.filter(question_id = this_id, has_teacher_answered = True)
            check = True
    else:
        no_answer = "Nie ma jeszcze odpowiedzi do tego pytania"

    return render(request, 'forum/question.html', {'this_question': this_question,'answers': answers,'no_answer':no_answer, 'teacher_answers': teacher_answers, 'check':check})

@login_required
def home(request):
    return render(request, 'forum/home.html') 

@login_required
def question_fake(request):
    tasks = upload_models.TaskList.objects.all()
    if request.method == "POST":
        question = Question()
        question.task_id = request.POST['ftask_id']
        question.question_content = request.POST['fcontent']
        question.asking_student = request.user.snumber
        question.save()
        return all(request)
    return render(request, 'forum/add_question_fake.html', {'tasks': tasks})

@login_required
def add_question(request, id):
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.task_id=id
            object.asking_student=request.user.username
            object.save()
            return redirect('/forum/all/')
    else:
        form=AddQuestionForm()
    return render(request, 'forum/questionForm.html', {'form': form})

@login_required
def add_answer(request, id):
    if request.method == "POST":
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            task = Question.objects.get(id = id)
            if request.user.is_staff:
                task.has_teacher_answer = True
                object.has_teacher_answered = True
            object.task_id = task.task_id
            object.question_id = id
            object.who_answered = request.user.username
            object.save()
            task.save()
            path = f'/forum/{id}'
            return redirect(path)
    else:
        form=AddAnswerForm()         
    return render(request, 'forum/add_answer_form.html',{'form': form}) 

@login_required
def answer_fake(request):
    return render(request, 'forum/add_answer_fake.html')


