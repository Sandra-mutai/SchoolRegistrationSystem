# from django import forms
# from django.shortcuts import render
# from.form import TrainerRegistrationForms
# from.models import Trainer

# def register_trainer(request):
#     form=TrainerRegistrationForms()
#     return render(request,"register_trainer.html",{"form":form})

# def register_trainer(request):
#     if request.method=="POST":
#        form=TrainerRegistrationForms(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#        else:
#            print(form.errors)
#     else:
#         form=TrainerRegistrationForms()
#     return render(request,"register_trainer.html",{"form":form})

# def trainer_list(request):
#     trainer=Trainer.objects.all()
#     return render(request,"trainer_list.html",{ "trainers":trainer})
    


from django import forms
from django.shortcuts import render
from django.shortcuts import redirect

from student.forms import Fooform
from.form import TrainerRegistrationForms
# from.forms import Fooform
from.models import Trainer

def register_trainer(request):
    if request.method=="POST":
       form=TrainerRegistrationForms(request.POST , request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)
    else:
        form=TrainerRegistrationForms()
    return render(request,"register_trainer.html",{"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{ "trainers":trainers})

def edit_trainer(request, id):
    trainer=Trainer.objects.get(id=id)

    if request.method=="POST":
        form=TrainerRegistrationForms(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForms(instance=trainer)
        return render(request,"edit_trainer.html", {"form":form})


def trainer_profile(request, id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html", {"trainer":trainer})

def delete_trainer(request, id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect(trainer_list)


def test_view(request):
    if request.method == 'POST':
        form = Fooform(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("button")
    else:
        form = Fooform()
    return render(request, 'profile.html', locals())



