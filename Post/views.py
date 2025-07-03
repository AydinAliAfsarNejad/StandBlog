from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
# Create your views here.


def post_detail(request, pk):
    post = get_object_or_404(Article, id=pk)
    return render(request,"Post/post-details.html" , {"post":post})