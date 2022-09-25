import json
from django.shortcuts import render, redirect
from .models import HashRecommend, PlaceComment, Course, Place
from django.http import HttpResponse, JsonResponse

# Create your views here.
def main(request):
    hashs = HashRecommend.objects.all()
    return render(request, 'home.html', {'hashs':hashs})

def detail(request, place_id):
    place = Place.objects.get(pk=place_id)
    if request.method == 'POST':
        comment = request.POST['text']
        if (comment is not None) and (comment != ""):
            PlaceComment.objects.create(author=request.user, text=comment, place=place)
                 
    return render(request, 'detail.html', {'place':place})

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
    # places = request.user.course_set.all().place.all()
    return render(request, 'myfeed.html')

def scrap(request, place_id):
    jsonObject = json.loads(request.body)
    place = Place.objects.get(pk=place_id)
    content = jsonObject.get('content')
    if content == "True":
        place.scrap_cnt += 1
        place.save()
        request.user.placescrap.add(place)
    else:
        place.scrap_cnt -= 1
        place.save()
        request.user.placescrap.remove(place)

    return JsonResponse({'content':content})

def setcourse(request):
    return render(request, 'setcourse.html')    

def otherscourse(request):
    return render(request, 'otherscourse.html')

def otherscourseDetail(request):
    return render(request, "otherscourse-detail.html")