from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    saved_place = models.ForeignKey()
    course = models.ForeignKey()

class Place(models.Model):
    name = models.CharField()
    latitude = models.FloatField()
    longtitude = models.FloatField()
    description = models.TextField()
    category = models.CharField()
    like = models.IntegerField()
    photo = models.ForeignKey()

class Photo(models.Model):
    src = models.ImageField()

class Course(models.Model):
    name = models.CharField()
    place = models.ForeignKey()
    copyed_count = models.IntegerField()

class AdminPlace(models.Model):
    hash_category = models.CharField()
    writer = models.CharField()
    description = models.CharField()
    like = models.IntegerField()
    category = models.CharField()
    comment = models.ForeignKey()