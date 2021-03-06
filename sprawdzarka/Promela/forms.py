from users.models import Group
from django import forms
from .models import *
from django.forms import fields


class TeacherTaskForm(forms.ModelForm):
    group_ids = [str(elem) for elem in list(Group.objects.all().values_list('id', flat=True))]
    group_names = [str(elem) for elem in list(Group.objects.all().values_list('name', flat=True))]
    this_choices = []
    if len(group_ids) > 0 and len(group_names) > 0:
        for i,j in zip(group_ids, group_names):
            this_choices.append(tuple([i,j]))
    group = fields.ChoiceField(choices=this_choices)

    class Meta:
        model = TeacherTask
        fields = ('task_name','max_points','file','group',)

class StudentTaskForm(forms.ModelForm):
    task_id_data = [str(elem) for elem in list(TeacherTask.objects.all().values_list('id', flat=True))]
    task_names = [str(elem) for elem in list(TeacherTask.objects.all().values_list('task_name', flat=True))]
    this_choices = []
    if len(task_id_data) > 0:
        for i,j in zip(task_id_data,task_names) :
            this_choices.append(tuple([i,j]))
    task_id = fields.ChoiceField(label='Numer zadania', choices=this_choices)
    class Meta:
        model = StudentTask
        fields = ('task_file','task_id')