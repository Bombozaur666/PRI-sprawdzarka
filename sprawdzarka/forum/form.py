from django.db.models import fields
from django.forms import models


from .models import *
from django import forms

class AddQuestionForm(forms.ModelForm):
	class Meta:
		model = QuestionXML
		fields = ('question_content',)

class AddAnswerForm(forms.ModelForm):
	class Meta:
		model = AnswerXML
		fields= ('content',)