"""notice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path
from django.conf.urls import url,include
from compte.models import Profile,Etablissement,Classe,Note,Enseignant
from django.contrib.auth import views
#from compte.forms import LoginForm
from .import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    #path('admin/', admin.site.urls),
    
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# On ajoute dans i18n_patterns la liste des urls des pages a traduire 
urlpatterns += i18n_patterns(
    #url(r'^{}'.format(settings.DJANGO_ADMIN_URL), admin.site.urls),
    path('',views.home,name='home'),
    path('note/', include('note.urls',namespace="note")),
    path('etablissement/', include('etablissement.urls',namespace="etablissement")),
    path('enseignant/', include('enseignant.urls',namespace="enseignant")),
    path('compte/', include('compte.urls',namespace="compte")),
    path('classe/', include('classe.urls',namespace="classe")),
) 