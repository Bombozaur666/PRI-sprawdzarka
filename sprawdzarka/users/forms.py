from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'snumber', 'password1', 'password2')

