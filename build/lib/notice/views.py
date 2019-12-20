from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login


def home(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {})

            else:
                # Return an 'invalid login' error message.
                messages.error(request, 'nom utilisateur ou mot de passe incorrect')
        return render(request, 'compte/login.html', {})
    else:
        return render(request, 'home.html', {})