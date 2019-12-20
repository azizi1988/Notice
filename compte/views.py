from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Etablissement
from .models import Profile
from .forms import User_Form

from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your views here.
def login_user(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
    # Return an 'invalid login' error message.
            messages.error(request,'nom utilisateur ou mot de passe incorrect')
    return render(request,'compte/login.html',{})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_registration(request):
        if request.method == 'POST':
            form = User_Form(request.POST) #UserRegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                conf_password = form.cleaned_data['conf_password']
                Etablissement = form.cleaned_data['Etablissement']
                if password == conf_password:
                    user = User.objects.create_user(username=username, password=password)
                    profile = Profile.objects.get(user=user)
                    profile.Etablissement=Etablissement
                    profile.save()
                    messages.success(request,'Enregistrement avec succés {}'.format(user.username))
                    return HttpResponseRedirect(reverse('compte:login'))
                else:
                    messages.error(request ,'les mots de passe ne sont pas identiques!')
        else:
            form = User_Form()
        return render(request,'compte/register.html',{'form':form})