from django import forms
from django.shortcuts import render
from.form import CoursesRegistrationForms
from.models import Courses



def register_trainer(request):
    form=CoursesRegistrationForms()
    return render(request,"register_trainer.html",{"form":form})

def register_courses(request):
    if request.method=="POST":
       form=CoursesRegistrationForms(request.POST , request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)

    else:
        form=CoursesRegistrationForms()
    return render(request,"register_courses.html",{"form":form})


def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"courses_list.html",{ "courses":courses})



