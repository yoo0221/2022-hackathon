from django.shortcuts import render
from .models import HashRecommend, AdminPlace, AdminPlaceComment
# Create your views here.
def main(request):
    hashs = HashRecommend.objects.all()
    return render(request, 'home.html', {'hashs':hashs})

def detail(request, adminplace_id):
    adminplace = AdminPlace.objects.get(pk=adminplace_id)
    if request.method == 'POST':
        comment = request.POST['text']
        AdminPlaceComment.objects.create(author=request.user, text=comment, adminplace=adminplace)
    
    return render(request, 'detail.html', {'adminplace':adminplace})

def course(request):
    return render(request, 'course.html')
