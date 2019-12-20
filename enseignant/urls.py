from django.urls import path 
from django.conf.urls import url
from . import views


app_name="enseignant"
urlpatterns = [
    path('enseignant_register/', views.enseignant_register,name="enseignant_register"),
    path('enseignant_list/', views.enseignantlist,name="enseignant_list"),
    url(r'enseignant_update/(?P<id>[0-9]+)/$',views.enseignant_update,name="enseignant_update"),
    url(r'enseignant_delete/(?P<id>[0-9]+)/$',views.enseignant_delete,name='enseignant_delete'),    
]