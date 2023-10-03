from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def blog_view(request,**kwargs):
    current_time = timezone.now()
    posts = Post.objects.filter(status=True, published_date__lte=current_time).order_by('-published_date')
    if kwargs.get('cat_name'):
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('username'):
        posts = posts.filter(author__username=kwargs['username'])
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # Get the current time
    current_time = timezone.now()
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=current_time)
    all_posts = Post.objects.filter(status=True, published_date__lte=current_time).order_by('-published_date')
    current_index = list(all_posts).index(post)
    next_post = all_posts[current_index - 1] if current_index > 0 else None
    previous_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None
    post.counted_views += 1
    post.save()
    return render(request, 'blog/blog-single.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    })


def blog_search(request):
    query = request.GET.get('s')  # Retrieve the 's' parameter from the GET request
    posts = Post.objects.filter(status=1)

    if query:
        # Use 'icontains' for case-insensitive search in both title and content
        posts = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
