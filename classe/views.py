from django.core import serializers
from django.contrib import messages
from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
#from etablissement import forms
from compte.models import Classe ,Etablissement
from django.views.generic import CreateView
from .forms import classe_form_register ,classe_form_Updater
from django_tables2 import RequestConfig
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from rest_framework import generics


def classe_register(request):
    if request.method == 'POST':
        form = classe_form_register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enregistrement avec succés')
            return redirect('classe:classe_list')

    else:
        form = classe_form_register()
    return render(request, 'classe_register.html', {'form': form})

def classe_list(request):
    all_classes = Classe.objects.all()
    return render(request, 'classe_list.html', {'all_classes': all_classes})

def classe_listing(request,id):
    etablissement = Etablissement.objects.get(id=id)
    all_classes = Classe.objects.filter(classe_code=etablissement)
    return render(request, 'classe_list.html', {'all_classes': all_classes})

def classe_update(request,id):
    if request.method == 'POST':
        obj=Classe.objects.get(id=id)
        form =classe_form_Updater(request.POST or None, instance= obj)
        
        if form.is_valid():
        
            obj= form.save(commit=False)
            obj.save()
            messages.success(request,'Mise à jour avec succés')
            return redirect('classe:classe_list')#, {'all_immobs': Immob.objects.all()})
    else:
        classes = Classe.objects.get(id=id)
        form=classe_form_Updater(instance=classes)
    
    return render(request, 'classe_update.html', {'form': form})

def classe_delete(request,id):
    instance = Classe.objects.get(id=id)
    instance.delete()
    return redirect('classe:classe_list')
