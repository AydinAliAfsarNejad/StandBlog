from django.contrib import admin
from .models import Article , Categorys , Comments
# Register your models here.

admin.site.register(Comments)
admin.site.register(Categorys)
admin.site.register(Article)