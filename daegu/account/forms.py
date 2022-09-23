from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password']
