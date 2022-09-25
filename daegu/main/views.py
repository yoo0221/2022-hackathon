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

def otherscourse(request):
    courses = Course.objects.all().order_by('scrap_cnt')
    return render(request, 'otherscourse.html', {"courses":courses})

def otherscourseDetail(request):
    return render(request, "otherscourse-detail.html")

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
    places_sick = request.user.placescrap.all().filter(category="식당")
    places_ca = request.user.placescrap.all().filter(category="카페")
    places_ja = request.user.placescrap.all().filter(category="자연")
    places_yeo = request.user.placescrap.all().filter(category="여가/활동")
    print(places_sick)
    print(places_ca)
    print(places_ja)
    print(places_yeo)
    return render(request, 'setcourse.html',
        {"places_sick" : places_sick,
        "places_ca" : places_ca,
        "places_ja" : places_ja,
        "places_yeo" : places_yeo}) 

def scrapcourse(request, course_id):
    jsonObject = json.loads(request.body)
    course = Course.objects.get(pk=course_id)
    content = jsonObject.get('content')
    if content == "True":
        course.scrap_cnt += 1
        course.save()
        request.user.coursescrap.add(course)
    else:
        course.scrap_cnt -= 1
        course.save()
        request.user.coursescrap.remove(course)

    return JsonResponse({'content':content})
