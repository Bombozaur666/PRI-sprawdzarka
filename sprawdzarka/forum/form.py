from django.forms import models


from .models import Question
from django import forms



class AddQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question_content',)