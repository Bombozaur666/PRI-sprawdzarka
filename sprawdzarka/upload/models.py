from django.db import models

# Create your models here.
class SendedTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/sendedtasks/')
    max_point=models.CharField(max_length=3,default="0")
    point=models.CharField(max_length=100,default="0")
    has_been_tested = models.BooleanField(default=False)
    group = models.CharField(max_length=10, default="0")

    class Meta:
        ordering = ('group','taskid',)



class TaskList(models.Model):
    id = models.IntegerField(primary_key=True)
    taskname = models.CharField(max_length=200, default='Brak tytułu')
    tname = models.CharField(max_length=100)
    task = models.FileField(upload_to='task/tasklist/')

class Plagiat(models.Model):
    id = models.IntegerField(primary_key=True)
    snumber1 = models.CharField(max_length=6)
    snumber2 = models.CharField(max_length=6)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    plagiat = models.FloatField()

class Promela(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/Promela/Studentstask/')
    taskcopy = models.FileField(upload_to='task/Promela/Studentstaskcopies/')
    group = models.CharField(max_length=10, default="0")
    has_been_tested = models.BooleanField(default=False)
    class Meta:
        ordering = ('group','taskid',)

class Promela2(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/Promela/Studentstask/')
    output = models.FileField(upload_to='task/Promela/Studentoutput/')
    group = models.CharField(max_length=10, default="0")
    point=models.CharField(max_length=100,default="0")
    class Meta:
        ordering = ('group','taskid',)


class TaskListPromela(models.Model):
    id = models.IntegerField(primary_key=True)
    taskname = models.CharField(max_length=200,default="Brak Tytułu")
    task = models.FileField(upload_to='task/PromelaList/')
    ltl_file= models.FileField(upload_to='task/LTL/')
    max_points = models.CharField(max_length=100, default="0")
