from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password', 'profile_img']
