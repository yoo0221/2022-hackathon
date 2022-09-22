from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')