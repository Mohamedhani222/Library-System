from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def logout_view(request):
    logout(request)
    redirect("index")

def register(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login( request , user )
            messages.success(request ,"Registration successful.")
            return redirect('index')
    else :
        form =RegisterForm()

    return render(request , 'registration/register.html' , {'form' : form })
