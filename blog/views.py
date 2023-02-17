from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def home(request):
    all_posts = Post.newmanager.all()
    context = {
        'posts': all_posts,
    }
    return render(request, 'index.html', context)

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html',{'post': post})
    