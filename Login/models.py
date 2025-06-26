from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile/picture')
    userCode = models.CharField(max_length=12 , null=True)

    def __str__(self):
        return self.user.username
