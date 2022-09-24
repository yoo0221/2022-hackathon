from django.shortcuts import render, redirect
from .models import HashRecommend, AdminPlace, AdminPlaceComment, Course
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

def postcreate(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == "POST":
        for place in course.place.all():
            img = request.FILES['place-img-'+str(place.id)]
            description = request.POST['description-'+str(place.id)]
            hashtag = request.POST['hashtag-'+str(place.id)]
            place.img = img
            place.description = description
            place.hashtag = hashtag
            place.save()
        return redirect('postdetail', course_id)
    return render(request, 'postcreate.html', {"course":course})

def postdetail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'postdetail.html', {"course":course})