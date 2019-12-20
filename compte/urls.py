from django.urls import path
from . import views
app_name="compte"
urlpatterns = [
    path('login/', views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.user_registration,name="register")
]