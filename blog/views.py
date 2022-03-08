from .models import Post
from django.shortcuts import render


def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-publish_date')
    return render(request, 'blog/blog_list.html', {'posts': posts,})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})