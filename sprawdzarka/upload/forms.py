from django import forms
from .models import SendedTasks
from .models import TaskList
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
