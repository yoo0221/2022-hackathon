from django.db import models
from account.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class HashRecommend(models.Model):
    hash=models.CharField(max_length=30)

    def __str__(self):
        return self.hash

# class AdminPlace(models.Model):
#     author=models.CharField(max_length=50, null=True)
#     profile_img=models.ImageField(null=True)
#     name=models.CharField(max_length=50)
#     description=models.TextField()
#     category=models.CharField(max_length=20,null=True)
#     scrap_cnt=models.IntegerField(default=0)
#     thumbnail=models.ImageField()
#     hashtag=models.ForeignKey(HashRecommend, on_delete=models.CASCADE, null=True)
#     lat=models.FloatField(null=True)
#     lng=models.FloatField(null=True)
#     address=models.CharField(max_length=100, null=True)
#     scrapper=models.ManyToManyField(User, blank=True, related_name="adminplacescrap")
    
#     def __str__(self):
#         return self.name



class Course(models.Model):
    name=models.CharField(max_length=50)
    scrap_cnt=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashtag=models.CharField(max_length=100, null=True, blank=True)
    scrapper=models.ManyToManyField(User, blank=True, related_name="coursescrap")
    thumbnail=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=50)
    img=models.ImageField(null=True, blank=True)
    scrap_cnt=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    category=models.CharField(max_length=20,null=True)
    hashtag=models.ForeignKey(HashRecommend, on_delete=models.CASCADE, null=True, blank=True)
    lat=models.FloatField()
    lng=models.FloatField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name="place")
    scrapper=models.ManyToManyField(User, blank=True, related_name="placescrap")


    def __str__(self):
        return self.name

class PlaceComment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    place=models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.text