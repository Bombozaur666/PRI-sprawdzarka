from django import forms
from .models import SendedTasks

class SendedTasksForm(forms.ModelForm):
    class Meta:
        model = SendedTasks
        fields = ('taskid','snumber','task')
class TasksListForm(forms.ModelForm):
	class Meta:
		labels = {
		"tname": "Teacher name"
		}
		model = TaskList
		fields = ('tname','task')
