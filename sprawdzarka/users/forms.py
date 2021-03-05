from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *
from django.forms import Form , fields, ModelForm

class RegistrationForm(UserCreationForm):
    group_ids = Group.objects.all()
    this_choices = []
    for i in group_ids:
        this_choices.append(tuple([str(i),str(i)]))
    group_id = fields.ChoiceField(choices=this_choices)
    class Meta:
        model = Account
        fields = ('username', 'snumber', 'password1', 'password2','group_id')

term_choices = (
        ('zima','Semestr Zimowy'),
        ('lato','Semestr Letni')
    ) 

class GroupForm(Form):
    name = fields.CharField(label='Nazwa grupy', max_length=255)
    year = fields.CharField(label='Rok akademicki', max_length=10)
    term = fields.ChoiceField(choices=term_choices)

class PassForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username','password1', 'password2')

    
