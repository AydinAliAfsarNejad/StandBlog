from django.contrib import admin
from .models import Article , Categorys
# Register your models here.

admin.site.register(Categorys)
admin.site.register(Article)