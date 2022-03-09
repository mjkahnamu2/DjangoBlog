from .models import Post
from django.shortcuts import render
from django.views.generic import ListView


def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-publish_date')
    return render(request, 'blog/blog_list.html', {'posts': posts,})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_post.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(title__icontains=query)
        return object_list