from django import forms
from .models import *
from django.forms import fields



class SendedTasksForm(forms.ModelForm):
	task_id_data = [str(elem) for elem in list(TaskList.objects.all().values_list('id', flat=True))]
	this_choices = []
	if len(task_id_data) > 0:
		for i in task_id_data :
			this_choices.append(tuple([i,i]))
	Plik = fields.ChoiceField(label='Numer zadania', choices=this_choices)
	class Meta:
		model = SendedTasks
		fields = ('task',)
		

class TasksListForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ('taskname','task',)



