from django import forms
from .models import *
from django.forms import fields

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('task', 'taskid')
		

class TasksListForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = ('taskname','task','group_id')

class TransformersForm(forms.Form):
    NewPoints=forms.IntegerField(label='Nowe punkty')
    class Meta:
	    fields = ('NewPoints',)

