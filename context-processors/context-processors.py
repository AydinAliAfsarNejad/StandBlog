from Post.models import Article , Categorys


def recent_Articles(request):
    recent_post = Article.objects.all().order_by('-created')[:3]
    categories = Categorys.objects.all()

    return {'recent_post': recent_post, 'categories': categories}