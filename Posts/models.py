from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
