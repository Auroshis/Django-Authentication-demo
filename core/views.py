from django.contrib.auth.models import User
#from django.contrib.auth import authenticate
#from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm
from django import forms
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#@login_required
def home(request):
    return render(request,'home.html')

# registration of new users method

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return render(request, 'home.html')    
            else:
                # username or email already exists part
                return render(request, 'login.html')
                
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})