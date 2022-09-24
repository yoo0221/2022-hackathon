from django.shortcuts import render, redirect
from django.contrib import auth
from account.models import User
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.profile_img = request.FILES['img']
            temp.save()
            print(temp)
            return redirect('login')
    else:
        form=RegisterForm()
        return render(request, 'register.html', {"form":form})

# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         img=request.FILES['img']
#         User.objects.create(username=username, password=password, profile_img=img)
#         return redirect('login')
#     else:
#         return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
    
    return render(request, 'login.html')