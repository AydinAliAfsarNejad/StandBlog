from django.shortcuts import render
from Post.models import Article


# Create your views here.

def home(request):
    articles = Article.objects.all()
    # articles = Article.objects.published()
    # articles = Article.objects.filter(is_published=True)
    return render(request, "Home_app/index.html", {'articles': articles})
