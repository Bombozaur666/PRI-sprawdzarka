from django.db import models


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_content = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, default="null")
    date = models.DateTimeField(auto_now_add= True)
    test = models.CharField(max_length=10)
    has_teacher_answered = models.BooleanField(default=False)

class QuestionPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_content = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)

class AnswerPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, default="null")
    date = models.DateTimeField(auto_now_add= True)
    test = models.CharField(max_length=10)
    has_teacher_answered = models.BooleanField(default=False)