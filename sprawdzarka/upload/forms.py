from django import forms
from .models import *
from django.forms import fields
import re

def return_points(file_1):
	suma=0
	lista = ""
	f = open(file_1, encoding="utf-8")
	for line in f:
		y = re.search(r'^<zadanie nr="(.+)" pkt="([0-9])">', line)
		if y is not None:
			lista += str(y.group(1)) + ": " + str(y.group(2)) + " "
			suma+=int(y.group(2))
	f.close()
	return lista, str(suma)

class SendedTasksForm(forms.ModelForm):
	task_id_data = [str(elem) for elem in list(TaskList.objects.all().values_list('id', flat=True))]
	
	this_choices = []
	if len(task_id_data) > 0:
		for i in task_id_data :
			this_choices.append(tuple([i,i]))
	taskid = fields.ChoiceField(choices=this_choices)
	class Meta:
		model = SendedTasks
		fields = ('task','task')


class SendedPromelaTasksForm(forms.ModelForm):
	task_id_data = [str(elem) for elem in list(TaskListPromela.objects.all().values_list('id', flat=True))]
	this_choices = []
	if len(task_id_data) > 0:
		for i in task_id_data:
			this_choices.append(tuple([i, i]))
	taskid = fields.ChoiceField(choices=this_choices)

	class Meta:
		model = Promela
		fields = ('taskid', 'task')

class TasksListForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ('taskname','task',)

class TaskListPromelaForm(forms.ModelForm):
	class Meta:
		model = TaskListPromela
		fields = ('taskname','task',)

