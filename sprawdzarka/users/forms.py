from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *
from django.forms import Form , fields

class RegistrationForm(UserCreationForm):
    group_ids = [str(elem) for elem in list(Group.objects.all().values_list('id', flat=True))]
    group_names = [str(elem) for elem in list(Group.objects.all().values_list('name', flat=True))]
    this_choices = []
    if len(group_ids) > 0 and len(group_names) > 0:
        for i,j in zip(group_ids, group_names):
            this_choices.append(tuple([i,j]))
    group = fields.ChoiceField(choices=this_choices)
    class Meta:
        model = Account
        fields = ('username', 'snumber', 'password1', 'password2','group')

term_choices = (
        ('zima','Semestr Zimowy'),
        ('lato','Semestr Letni')
    ) 

class GroupForm(Form):
    name = fields.CharField(label='Nazwa grupy', max_length=255)
    year = fields.CharField(label='Rok akademicki', max_length=10)
    term = fields.ChoiceField(choices=term_choices)

class ChangePasswordForm(Form):
    
