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
    places_sick = request.user.placescrap.all().filter(category="식당")
    places_ca = request.user.placescrap.all().filter(category="카페")
    places_ja = request.user.placescrap.all().filter(category="자연")
    places_yeo = request.user.placescrap.all().filter(category="여가/활동")
    aplaces_sick = request.user.adminplacescrap.all().filter(category="식당")
    aplaces_ca = request.user.adminplacescrap.all().filter(category="카페")
    aplaces_ja = request.user.adminplacescrap.all().filter(category="자연")
    aplaces_yeo = request.user.adminplacescrap.all().filter(category="여가/활동")
    print(places_sick)
    print(places_ca)
    print(places_ja)
    print(places_yeo)
    print(aplaces_sick)
    print(aplaces_ca)
    print(aplaces_ja)
    print(aplaces_yeo)
    return render(request, 'setcourse.html',
        {"places_sick" : places_sick,
        "places_ca" : places_ca,
        "places_ja" : places_ja,
        "places_yeo" : places_yeo,
        "aplaces_sick" : aplaces_sick,
        "aplaces_ca" : aplaces_ca,
        "aplaces_ja" : aplaces_ja,
        "aplaces_yeo" : aplaces_yeo})