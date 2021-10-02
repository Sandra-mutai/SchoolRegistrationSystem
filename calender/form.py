from django import forms
from .models import Calender


class CalenderRegistrationForms(forms.ModelForm):
    class Meta:
        model=Calender
        fields="__all__"

