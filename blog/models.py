from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    ('draft',"Draft"),
    ('published',"Publish")
)

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields for your Blog model

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields for your Post model

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Other fields for your Profile model
