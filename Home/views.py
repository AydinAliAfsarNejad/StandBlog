from django.shortcuts import render
from Post.models import Article


# Create your views here.
# request.resolver_match.url_name = 'home'
def home(request):
    articles = Article.objects.all()
    # articles = Article.custum_objects.filter()
    # articles = Article.objects.published()
    # articles = Article.objects.filter(is_published=True)
    recent_post = Article.objects.all().order_by('-created')[:2]
    return render(request, "Home_app/index.html", {'articles': articles})


