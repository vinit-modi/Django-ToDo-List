from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

def user_signup(request):
    if request.method == 'GET':
        return render(request,'todo/user_signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
            except IntegrityError:
                return render(request,'todo/user_signup.html',{'form':UserCreationForm(), 'error':'That username has been already taken. Choose another one.'})
        else:
             return render(request,'todo/user_signup.html',{'form':UserCreationForm(), 'error':'Passwords didn\'t match'})
