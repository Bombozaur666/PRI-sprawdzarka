from django import forms
from .models import *
from django.forms import fields
from users.models import *

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class ChooseGroup(forms.Form):
    this_choices = []
    group_names=[str(elem) for elem in list(Group.objects.all().values_list('name', flat=True))]
    group_ids=[str(elem) for elem in list(Group.objects.all().values_list('id', flat=True))]
    if len(group_ids) != 0:
        for i,j in zip(group_names,group_ids):
            this_choices.append((j,i))
    group = forms.ChoiceField(choices=this_choices)
    plagiarism = forms.FloatField()
    class Meta:
        fields = ('group','plagiarism',)

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('task', 'taskid')
		

class TasksListForm(forms.ModelForm):
    date_end = forms.DateTimeField(widget=DateInput)
    class Meta:
        model = TaskList
        fields = ('taskname','task','group_id','date_end',)
        
class TransformersForm(forms.Form):
    NewPoints=forms.IntegerField(label='Nowe punkty')
    class Meta:
        fields = ('NewPoints',)




