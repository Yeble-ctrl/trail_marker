from django.db import models
from django.contrib.auth.models import User
from userProfile.models import user_directory_path

class Blog(models.Model):
    owner = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

class BlogPostPhoto(models.Model):
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)