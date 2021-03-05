from django.db import models


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_content = models.TextField("Zadaj pytanie", max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answer = models.BooleanField(default= False)
    asking_student = models.CharField(max_length= 6)
    class Meta:
        ordering = ('-date',)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    question_id = models.IntegerField()
    who_answered = models.CharField(max_length= 30)
    content = models.TextField(max_length=1024, blank=False, default=None)
    date = models.DateTimeField(auto_now_add= True)
    has_teacher_answered = models.BooleanField(default=False)