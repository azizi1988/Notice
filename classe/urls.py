from django.urls import path 
from django.conf.urls import url
from . import views


app_name="classe"
urlpatterns = [
    path('classe_register/', views.classe_register,name="classe_register"),
    path('classe_list/', views.classe_list,name="classe_list"),
    url(r'classe_list/(?P<id>[0-9]+)/$',views.classe_listing,name="classe_listing"),
    url(r'classe_update/(?P<id>[0-9]+)/$',views.classe_update,name="classe_update"),
    url(r'classe_delete/(?P<id>[0-9]+)/$',views.classe_delete,name="classe_delete"),    
]