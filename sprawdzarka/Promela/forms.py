from users.models import Group
from django import forms
from .models import *
from django.forms import fields
import re

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
        fields = ('task_name','max_points','file','group')

class StudentTaskForm(forms.ModelForm):
    class Meta:
        model = StudentTask
        fields = ('task_file',)