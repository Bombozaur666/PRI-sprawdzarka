from django.db import models
from Promela.models import *
from upload.models import *


class QuestionXML(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(TaskList, on_delete=CASCADE)
    question_content = models.TextField("Zadaj pytanie", max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)
    class Meta:
        ordering = ('-date',)

class AnswerXML(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answered = models.BooleanField(default=False)

class QuestionPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(TeacherTask, on_delete=CASCADE)
    question_content = models.TextField("Zadaj pytanie", max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)
    class Meta:
        ordering = ('-date',)

class AnswerPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answered = models.BooleanField(default=False)