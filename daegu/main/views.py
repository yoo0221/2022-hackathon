from django.shortcuts import render
from .models import HashRecommend, AdminPlace
# Create your views here.
def main(request):
    hashs = HashRecommend.objects.all()
    return render(request, 'home.html', {'hashs':hashs})

def detail(request, adminplace_id):
    adminplace = AdminPlace.objects.get(pk=adminplace_id)
    return render(request, 'detail.html', {'adminplace':adminplace})

def course(request):
    return render(request, 'course.html')
