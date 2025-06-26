from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorys(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100, unique=True, help_text="enter the article title")
    category = models.ManyToManyField(Categorys)
    body = models.TextField()
    image = models.ImageField(upload_to="images/article")
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    # published = models.BooleanField(default=True)
    # is_published = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f"{self.title} --- {self.body[:30]}"
