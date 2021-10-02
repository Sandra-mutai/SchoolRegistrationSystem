from django import forms
from .models import Student


class StudentRegistrationForms(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class Fooform(forms.Form):
    button = forms.CharField()
