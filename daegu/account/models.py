from django.db import models
from django.contrib.auth.models import AbstractUser
# from .temp_models import AdminPlace, Place, Course

# Create your models here.
class User(AbstractUser):
    profile_img=models.ImageField()