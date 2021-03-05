from django.db.models import fields
from django.forms import models


from .models import Question,Answer
from django import forms

class AddQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question_content',)

class AddAnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields= ('content',)