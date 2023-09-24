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

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def blog_single(request, pid):
    # Get the current time
    current_time = timezone.now()

    # Retrieve the current post and make sure it's published
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=current_time)

    # Get all published posts ordered by published date
    all_posts = Post.objects.filter(status=True, published_date__lte=current_time).order_by('-published_date')

    # Find the index of the current post in the list
    current_index = list(all_posts).index(post)

    # Determine the next and previous posts based on the current post's position
    next_post = all_posts[current_index - 1] if current_index > 0 else None
    previous_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None

    # Increment the view count of the current post
    post.counted_views += 1
    post.save()

    # Render the 'blog/blog-single.html' template with the post and navigation data
    return render(request, 'blog/blog-single.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    })
