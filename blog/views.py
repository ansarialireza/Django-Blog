from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse

def blog_view(request):
    current_time = timezone.now()
    published_posts = Post.objects.filter(status=True, published_date__lte=current_time).order_by('-published_date')
    context = {'posts': published_posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    current_time = timezone.now()
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=current_time)
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)