from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from.forms import Fooform, StudentRegistrationForms
from.models import Student

def register_student(request):
    if request.method=="POST":
       form=StudentRegistrationForms(request.POST , request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)
    else:
        form=StudentRegistrationForms()
    return render(request,"register_student.html",{"form":form})

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{ "students":students})

def edit_student(request, id):
    student=Student.objects.get(id=id)

    if request.method=="POST":
        form=StudentRegistrationForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
    else:
        form=StudentRegistrationForms(instance=student)
        return render(request,"edit_student.html", {"form":form})


def student_profile(request, id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html", {"student":student})

def delete_student(request, id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect(student_list)


def test_view(request):
    if request.method == 'POST':
        form = Fooform(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("button")
    else:
        form = Fooform()
    return render(request, 'profile.html', locals())




