from telnetlib import AUTHENTICATION
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserLoginForm
urlpatterns = [
    path('login' , LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register' , views.register , name='register'),
    path('logout', LogoutView.as_view(next_page = 'login') , name='logout'),
]