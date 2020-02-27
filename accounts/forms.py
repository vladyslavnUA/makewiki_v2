from .models import Question
from django import forms

class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birthdate = forms.DateField()

class QuestionCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birthdate = forms.DateField()