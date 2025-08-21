from django.shortcuts import render, get_object_or_404, redirect
from .models import Article , Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



def post_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    comments = Comments.objects.filter(article=post)

    if request.method == 'POST':
        body = request.POST.get('message')
        if request.user.is_authenticated and body:
            Comments.objects.create(body=body, article=post, author=request.user)
            return redirect('Post_details', slug=post.slug)
        else:
            return redirect('login:login')

    return render(request,"Post/post-details.html", {"post":post , "comments":comments})


def post_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "Post/post-list.html", {'articles': object_list})

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)

    return render(request, "Post/post-list.html", {'articles': object_list})