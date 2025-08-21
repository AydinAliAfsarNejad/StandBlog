from django.db import models
from django.contrib.auth.models import User

class Categorys(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # تصحیح: author نه auther
    title = models.CharField(max_length=100, unique=True, help_text="عنوان مقاله")
    category = models.ManyToManyField(Categorys)
    body = models.TextField()
    image = models.ImageField(upload_to="images/article")
    created = models.DateTimeField(auto_now=True)      # تاریخ بروزرسانی
    updated = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    slug = models.SlugField(unique=True, help_text="اسلاگ مقاله")

    class Meta:
        ordering = ['updated']

    def __str__(self):
        return f"{self.title} --- {self.body[:30]}"

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.body[:50]}"