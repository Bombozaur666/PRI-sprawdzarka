from django.db import models

# Create your models here.
class SendedTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.CharField(max_length=5)
    snumber = models.CharField(max_length=6)
    task = models.FileField(upload_to='task/sendedtasks/')
    max_point=models.CharField(max_length=3,default="0")
    point=models.CharField(max_length=100,default="0")


class TaskList(models.Model):
	id = models.IntegerField(primary_key=True)
	tname = models.CharField(max_length=100)
	task = models.FileField(upload_to='task/tasklist/')
