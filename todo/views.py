from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def user_signup(request):
    if request.method == 'GET':
        return render(request,'todo/user_signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/user_signup.html',{'form':UserCreationForm(), 'error':'That username has been already taken. Choose another one.'})
        else:
             return render(request,'todo/user_signup.html',{'form':UserCreationForm(), 'error':'Passwords didn\'t match'})

def user_login(request):
    if request.method == 'GET':
        return render(request,'todo/user_login.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request,'todo/user_login.html',{'form':AuthenticationForm(), 'error':'username and password did not match.'})
        else:
            login(request, user)
            return redirect('currenttodos')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def currenttodos(request):
    return render(request,'todo/currenttodos.html')

