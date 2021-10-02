from django import forms
from django.shortcuts import render
from.form import CalenderRegistrationForms
from.models import Calender



def register_calender(request):
    form=CalenderRegistrationForms()
    return render(request,"register_trainer.html",{"form":form})

def register_calender(request):
    if request.method=="POST":
       form=CalenderRegistrationForms(request.POST , request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)
    else:
        form=CalenderRegistrationForms()
    return render(request,"register_calender.html",{"form":form})

def calender_list(request):
    calenders=Calender.objects.all()
    return render(request,"calender_list.html",{ "calenders":calenders})

