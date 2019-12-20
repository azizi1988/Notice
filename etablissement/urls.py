from django.urls import path 
from django.conf.urls import url
from . import views


app_name="etablissement"
urlpatterns = [
    path('etablissement_register/', views.etablissement_register,name="etab_register"),
    path('etablissement_list/', views.etablissement_list,name="etab_list"),
    url(r'etablissement_update/(?P<id>[0-9]+)/$',views.etablissement_update,name="etab_update"),
    url(r'etablissement_delete/(?P<id>[0-9]+)/$',views.etablissement_delete,name='etab_delete'),    
]