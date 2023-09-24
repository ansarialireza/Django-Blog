from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=31)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)  # Add author as a foreign key
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    counted_comment = models.IntegerField(default=0)
    category=models.ManyToManyField(Category)
    image = models.ImageField(upload_to='post_images/') 
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "{}-{}".format(self.title, self.id)

