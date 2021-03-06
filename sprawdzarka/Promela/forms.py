from users.models import Group
from django import forms
from .models import *
from django.forms import fields


class TeacherTaskForm(forms.ModelForm):
    class Meta:
        model = TeacherTask
        fields = ('task_name','max_points','file','group_id',)

class StudentTaskForm(forms.ModelForm):
    class Meta:
        model = StudentTask
        fields = ('task_file','task_id')