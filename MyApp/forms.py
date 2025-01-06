from django.forms import ModelForm
from .models import Person

class PersonLogupForm(ModelForm):
    class Meta:
        model = Person
        fields = ['dni', 'name', 'email', 'password']

class PersonLoginForm(ModelForm):
    class Meta:
        model = Person
        fields = ['dni', 'password']
        