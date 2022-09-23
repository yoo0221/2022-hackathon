from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

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