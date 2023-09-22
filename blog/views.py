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
    
    # Get a list of all posts ordered by published date
    all_posts = list(Post.objects.filter(status=True, published_date__lte=current_time).order_by('-published_date'))
    
    # Find the index of the current post
    current_index = None
    for i, p in enumerate(all_posts):
        if p == post:
            current_index = i
            break
    
    # Check if there is a previous and/or next post
    next_post = all_posts[current_index - 1] if current_index > 0 else None
    previous_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    
    # Update the viewed post count
    post.counted_views += 1
    post.save()
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-single.html', context)
