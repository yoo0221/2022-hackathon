"""daegu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('detail/<int:place_id>', views.detail, name="detail"),
    path('account/', include('account.urls')),
    path('course/', views.course, name="course"),
    path('postcreate/<int:course_id>', views.postcreate, name="postcreate"),
    path('postdetail/<int:course_id>', views.postdetail, name="postdetail"),
    path('myfeed/', views.myfeed, name="myfeed"),
    path('scrap/<int:place_id>', views.scrap, name="scrap"),
    path('setcourse/', views.setcourse, name="setcourse"),
    path('otherscourse/', views.otherscourse, name="otherscourse"),
    path('otherscourseDetail/', views.otherscourseDetail, name="otherscourseDetail"),
    path('scrapcourse/<int:course_id>', views.scrapcourse, name="scrapcourse"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

