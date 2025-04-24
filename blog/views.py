from blog import models, serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsOwnerOrReadOnly

# Views for the Blog model
class Blogs(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Views for the BlogPost model
class BlogPosts(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = [IsAuthenticated]

class BlogPostDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

# Views for the BlogPostPhoto model
class BlogPostPhotos(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """
    queryset = models.BlogPostPhoto.objects.all()
    serializer_class = serializers.BlogPostPhotoSerializer
    permission_classes = [IsAuthenticated]

class BlogPostPhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for Get, Put, Patch and Delete requests
    """
    queryset = models.BlogPostPhoto.objects.all()
    serializer_class = serializers.BlogPostPhotoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]