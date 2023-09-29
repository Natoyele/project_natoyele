from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ForetForm, VillageForm, Foret_Sacree_Form
# Create your views here.

def villageCreate(request):
    form = VillageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VillageForm()
    return render(request, "village.html", {"form": form})

def ForetCreate(request):
    form = ForetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ForetForm()
    return render(request, "foret.html", {"form": form})

def Foret_Sacree_Create(request):
    form = Foret_Sacree_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Foret_Sacree_Form()
    return render(request, "foret_sacree.html", {"form": form})