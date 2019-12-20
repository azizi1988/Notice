from django.core import serializers
from django.contrib import messages
from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from note import forms
from compte.models import Note, Classe
from django.views.generic import CreateView
from .forms import note_register_form,note_update_form,note_read_form
from django_tables2 import RequestConfig
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage 


def note_register(request):
    if request.method == 'POST'  and request.FILES['document'] :
        form = note_register_form(request.POST,request.FILES)
        if form.is_valid():
            document = request.FILES['document']
            fs = FileSystemStorage()
            filename = fs.save(document.name, document)
            uploaded_file_url = fs.url(filename)
            form.save()
            messages.success(request,'Enregistrement avec succés')
            return render(request,'note_list.html',{'uploaded_file_url': uploaded_file_url})

    else:
        form = note_register_form()
    return render(request, 'note_register.html', {'form': form})

def note_list(request):
    all_notes = Note.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_notes,13)
    try:
        all_notes = paginator.page(page)
    except PageNotAnInteger:
        all_notes = paginator.page(1)
    except EmptyPage:
        all_notes = paginator.page(paginator.num_pages)
    return render(request, 'note_list.html', {'all_notes': all_notes})

def note_listing(request,id):
    classe = Classe.objects.get(id=id)
    all_notes= Note.objects.filter(classe=classe)
    page = request.GET.get('page',1)
    paginator = Paginator(all_notes,13)
    try:
        all_notes = paginator.page(page)
    except PageNotAnInteger:
        all_notes = paginator.page(1)
    except EmptyPage:
        all_notes = paginator.page(paginator.num_pages)
    return render(request, 'note_list.html', {'all_notes': all_notes})

def note_update(request,id):
    if request.method == 'POST':
        obj=Note.objects.get(id=id)
        form=note_update_form(request.POST or None, instance= obj)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request,'Mise à jour avec succés')
            return redirect('note:note_list') #, {'all_immobs': Immob.objects.all()})
    else:
        note = Note.objects.get(id=id)
        form=forms.note_update_form(instance=note)
    return render(request, 'note_update.html', {'form': form})

def note_delete(request,id):
    instance = Note.objects.get(id=id)
    instance.delete()
    return redirect('note:note_list')

def note_read(request,id):
    if request.method == 'POST':
        obj=Note.objects.get(id=id)
        form=note_read_form(request.POST or None, instance= obj)
        if form.is_valid():
            obj= form.save(commit=False)
            obj.save()
            messages.success(request,'Mise à jour avec succés')
            return redirect('note:note_list') #, {'all_immobs': Immob.objects.all()})
    else:
        note = Note.objects.get(id=id)
        form=forms.note_read_form(instance=note)
    return render(request, 'note_read.html', {'form': form})
