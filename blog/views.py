from django.contrib.auth.models import User
from blog import models, serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwnerOrReadOnly

# Views for the Blog model
class Blogs(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """

# Views for the BlogPost model
class BlogPosts(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """

class BlogPostDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """

# Views for the BlogPostPhoto model
class BlogPostPhotos(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """

class BlogPostPhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """