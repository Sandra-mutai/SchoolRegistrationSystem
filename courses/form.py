from django import forms
from django.forms import fields
from django.db import models
from .models import Courses


class CoursesRegistrationForms(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"