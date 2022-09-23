from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()
        return render(request, 'register.html', {"form":form})

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
    
    return render(request, 'login.html')