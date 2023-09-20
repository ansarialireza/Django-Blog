from django.contrib import admin
from blog.models import Post,Author
# Register your models here.


# @admin.register(post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status',
                    'published_date', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the Author model with its corresponding admin class
admin.site.register(Author, AuthorAdmin)
