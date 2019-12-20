from django.urls import path 
from django.conf.urls import url
from . import views


app_name="note"
urlpatterns = [
    path('note_register/', views.note_register,name="note_register"),
    path('note_list/', views.note_list,name="note_list"),
    url(r'note_list/(?P<id>[0-9]+)/$',views.note_listing,name="note_listing"),
    url(r'note_update/(?P<id>[0-9]+)/$',views.note_update,name="note_update"),
    url(r'note_read/(?P<id>[0-9]+)/$',views.note_read,name="note_read"),
    url(r'note_delete/(?P<id>[0-9]+)/$',views.note_delete,name='note_delete'),    
]