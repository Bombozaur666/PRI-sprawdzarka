from django.shortcuts import render, redirect
from .models import *
from upload import models as upload_models
from django.contrib.auth.decorators import login_required

@login_required
def all_normal(request):
    all_questions = Question.objects.all()
    return render(request, 'forum/all_questions.html', {'all':all_questions})

@login_required
def all_promela(request):
    all_questions = QuestionPromela.objects.all()
    return render(request, 'forum/all_promela.html', {'all':all_questions})

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
def question_promela(request, id):
    this_id = id
    this_question = QuestionPromela.objects.get(id = this_id)
    no_answer = ''
    teacher_answers = []
    answers = []
    check = False
    if AnswerPromela.objects.filter(question_id = this_id).exists():
        answers = AnswerPromela.objects.filter(question_id = this_id, has_teacher_answered = False)
        if AnswerPromela.objects.filter(question_id = this_id, has_teacher_answered = True).exists():
            teacher_answers = AnswerPromela.objects.filter(question_id = this_id, has_teacher_answered = True)
            check = True
    else:
        no_answer = "Nie ma jeszcze odpowiedzi do tego pytania"

    return render(request, 'forum/question_promela.html', {'this_question': this_question,'answers': answers,'no_answer':no_answer, 'teacher_answers': teacher_answers, 'check':check})

@login_required
def home(request):
    return render(request, 'forum/home.html') 

@login_required
def home_promela(request):
    return render(request, 'forum/home_promela.html') 

@login_required
def choose(request):
    return render(request, 'forum/choose.html') 

@login_required
def question_fake(request):
    tasks = upload_models.TaskList.objects.all()
    if request.method == "POST":
        question = Question()
        question.task_id = request.POST['ftask_id']
        question.question_content = request.POST['fcontent']
        question.asking_student = request.user.snumber
        question.save()
        return all_normal(request)
    return render(request, 'forum/add_question_fake.html', {'tasks': tasks})

@login_required
def question_fake_promela(request):
    tasks = upload_models.TaskListPromela.objects.all()
    if request.method == "POST":
        question = QuestionPromela()
        question.task_id = request.POST['ftask_id']
        question.question_content = request.POST['fcontent']
        question.asking_student = request.user.snumber
        question.save()
        return all_promela(request)
    return render(request, 'forum/add_question_fake_promela.html', {'tasks': tasks})

@login_required
def add_question(request, id):
    this_id = id
    if request.method == "POST":
        question = Question()
        question.task_id = this_id
        question.question_content = request.POST['fcontent']
        question.asking_student = request.user.snumber
        question.save()
        return all(request)
    return render(request, 'forum/add_question.html')


@login_required
def add_answer(request, id):
    question_id = id
    task = Question.objects.get(id = question_id)
    task_id = task.task_id
    if request.method == 'POST':
        answer = Answer()
        if request.user.is_staff:
            answer.has_teacher_answered = True
            task.has_teacher_answer = True
        answer.task_id = task_id
        answer.question_id = question_id
        answer.content = request.POST['fcontent']
        answer.who_answered = request.user.username
        answer.save()
        task.save()
        return question(request, id)

    return render(request, 'forum/add_answer.html') 

@login_required
def add_answer_promela(request, id):
    question_id = id
    task = QuestionPromela.objects.get(id = question_id)
    task_id = task.task_id
    if request.method == 'POST':
        answer = AnswerPromela()
        if request.user.is_staff:
            answer.has_teacher_answered = True
            task.has_teacher_answer = True
        answer.task_id = task_id
        answer.question_id = question_id
        answer.content = request.POST['fcontent']
        answer.who_answered = request.user.username
        answer.save()
        task.save()
        return question_promela(request, id)

    return render(request, 'forum/add_answer_promela.html') 



