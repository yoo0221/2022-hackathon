import json
from django.shortcuts import render, redirect
from .models import HashRecommend, AdminPlace, AdminPlaceComment, Course
from django.http import HttpResponse, JsonResponse

# Create your views here.
def main(request):
    hashs = HashRecommend.objects.all()
    return render(request, 'home.html', {'hashs':hashs})

def detail(request, adminplace_id):
    adminplace = AdminPlace.objects.get(pk=adminplace_id)
    if request.method == 'POST':
        comment = request.POST['text']
        if (comment is not None) and (comment != ""):
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
            hashtag = request.POST['hashtag']
            place.img = img
            place.description = description
            course.hashtag = hashtag
            place.save()
            course.save()
        return redirect('postdetail', course_id)
    return render(request, 'postcreate.html', {"course":course})

def postdetail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'postdetail.html', {"course":course})

def myfeed(request):
    return render(request, 'myfeed.html')

def scrap(request, course_id):
    jsonObject = json.loads(request.body)
    adminplace = AdminPlace.objects.get(pk=course_id)
    content = jsonObject.get('content')
    if content == "True":
        adminplace.scrap_cnt += 1
        adminplace.save()
        request.user.adminplacescrap.add(adminplace)
    else:
        adminplace.scrap_cnt -= 1
        adminplace.save()
        request.user.adminplacescrap.remove(adminplace)

    return JsonResponse({'content':content})

def setcourse(request):
    return render(request, 'setcourse.html')    