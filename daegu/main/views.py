from django.shortcuts import render
from .models import HashRecommend
# Create your views here.
def main(request):
    hashs = HashRecommend.objects.all()
    return render(request, 'home.html', {'hashs':hashs})

def detail(request):
    return render(request, 'detail.html')

def course(request):
    return render(request, 'course.html')