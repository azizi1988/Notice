from django.core import serializers
from django.contrib import messages
from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
#from etablissement import forms
from compte.models import Etablissement
from django.views.generic import CreateView
from .forms import etablissement_form_register ,etablissement_form_Updater
from django_tables2 import RequestConfig
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator


def etablissement_register(request):
    if request.method == 'POST':
        form = etablissement_form_register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enregistrement avec succés')
            return redirect('etablissement:etab_list')

    else:
        form = etablissement_form_register()
    return render(request, 'etab_register.html', {'form': form})

def etablissement_list(request):
    all_etablissements = Etablissement.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_etablissements,13)
    try:
        all_etablissements = paginator.page(page)
    except PageNotAnInteger:
        all_etablissements = paginator.page(1)
    except EmptyPage:
        all_etablissements = paginator.page(paginator.num_pages)
    return render(request, 'etab_list.html', {'all_etablissements': all_etablissements})

def etablissement_update(request,id):
    if request.method == 'POST':
        obj=Etablissement.objects.get(id=id)
        form =etablissement_form_Updater(request.POST or None, instance= obj) 
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request,'Mise à jour avec succés')
            return redirect('etablissement:etab_list')#, {'all_immobs': Immob.objects.all()})
    else:
        etablissment = Etablissement.objects.get(id=id)
        form =etablissement_form_Updater(instance=Etablissement.objects.get(id=id))
    
    return render(request, 'etab_update.html', {'form': form})

def etablissement_delete(request,id):
    instance = Etablissement.objects.get(id=id)
    instance.delete()
    return redirect('etablissement:etab_list')





        




