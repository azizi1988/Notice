from django.core import serializers
from django.contrib import messages
from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
#from etablissement import forms
from compte.models import Enseignant
from django.views.generic import CreateView
from .forms import enseignant_form_Register,enseignant_form_Update
from django_tables2 import RequestConfig
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from rest_framework import generics


def enseignant_register(request):
    if request.method == 'POST':
        form = enseignant_form_Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enregistrement avec succés')
            return redirect('enseignant:enseignant_list')

    else:
        form = enseignant_form_Register()
    return render(request, 'enseignant_register.html', {'form': form})

def enseignantlist(request):
    all_enseigants = Enseignant.objects.all()
    return render(request, 'enseignant_list.html', {'all_enseigants': all_enseigants })

def enseignant_update(request,id):
    if request.method == 'POST':
        obj=Enseignant.objects.get(id=id)
        form =enseignant_form_Update(request.POST or None, instance= obj)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request,'Mise à jour avec succés')
            return redirect('enseignant:enseignant_list')#, {'all_immobs': Immob.objects.all()})
    else:
        enseignant = Enseignant.objects.get(id=id)
        form=enseignant_form_Update(instance=enseignant)
    return render(request, 'enseignant_update.html', {'form': form})

def enseignant_delete(request,id):
    instance = Enseignant.objects.get(id=id)
    instance.delete()
    return redirect('enseignant:enseignant_list')

