from django.db import models
from django.contrib.auth.models import AbstractUser
from account.models import User

# Create your models here.
class HashRecommend(models.Model):
    hash=models.CharField(max_length=30)

    def __str__(self):
        return self.hash

class AdminPlace(models.Model):
    author=models.CharField(max_length=50, null=True)
    profile_img=models.ImageField(null=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.CharField(max_length=20)
    scrap_cnt=models.IntegerField(default=0)
    thumbnail=models.ImageField()
    hashtag=models.ForeignKey(HashRecommend, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class AdminPlaceComment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    adminplace=models.ForeignKey(AdminPlace, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Course(models.Model):
    name=models.CharField(max_length=50)
    scrap_cnt=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hashtag=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(null=True, blank=True)
    address=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    lat=models.FloatField()
    lng=models.FloatField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name="place")

    def __str__(self):
        return self.name

# class Place(models.Model):
#     author=models.ForeignKey(User, null=True)
#     profile_img=models.ImageField(null=True)
#     name=models.CharField(max_length=50)
#     description=models.TextField()
#     category=models.CharField(max_length=20)
#     scrap_cnt=models.IntegerField(default=0)
#     thumbnail=models.ImageField()
#     hashtag=models.ForeignKey(HashRecommend, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.name


# class ScrappedPlace(models.Model):
#     name = models.CharField()
#     lat = models.FloatField()
#     lng = models.FloatField()
#     description = models.TextField()
#     category = models.CharField()
#     like = models.IntegerField()

# class Photo(models.Model):
#     src = models.ImageField()
#     scrappedplace = models.ForeignKey(ScrappedPlace, on_delete=False)

# class Course(models.Model):
#     name = models.CharField()
#     copyed_count = models.IntegerField()

# class Place(models.Model):
#     name = models.CharField()
#     latitude = models.FloatField()
#     longtitude = models.FloatField()
#     description = models.TextField()
#     category = models.CharField()
#     like = models.IntegerField()

# class Place(models.Model):
#     name = models.CharField()
#     latitude = models.FloatField()
#     longtitude = models.FloatField()
#     description = models.TextField()
#     category = models.CharField()
#     like = models.IntegerField()
#     photo = models.ForeignKey()

# class Photo(models.Model):
#     src = models.ImageField()

# class Course(models.Model):
#     name = models.CharField()
#     place = models.ForeignKey()
#     copyed_count = models.IntegerField()

# class AdminPlace(models.Model):
#     hash_category = models.CharField()
#     writer = models.CharField()
#     description = models.CharField()
#     like = models.IntegerField()
#     category = models.CharField()
#     comment = models.ForeignKey()