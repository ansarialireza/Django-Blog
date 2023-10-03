from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag('website/index-blog.html')
def display_latest_posts():
    posts=Post.objects.order_by('-published_date')[0:6]
    return {'posts':posts}