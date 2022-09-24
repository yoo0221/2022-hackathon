from django.shortcuts import render, redirect
from django.contrib import auth
from account.models import User

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        profile=request.FILES['profile']
        user = User.objects.create(username=username, password=password, profile_img=profile)
        auth.login(request, user)
        return redirect('main')
    return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
    return render(request, 'login.html')
