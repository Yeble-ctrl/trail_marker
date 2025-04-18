from django.urls import path
from blog import views

urlpatterns = [
    # URL patterns for the Blog model
    path('blogs/', views.Blogs.as_view()),
    path('blogs/<int:pk>/', views.BlogDetails.as_view()),

    # URL patterns for the BlogPost model
    path('blog-posts/', views.BlogPosts.as_view()),
    path('blog-posts/<int:pk>/', views.BlogPostDetails.as_view()),

    # URL patterns for the BlogPostPhoto model
    path('blog-post-photos/', views.BlogPostPhotos.as_view()),
    path('blog-post-photos/<int:pk>/', views.BlogPostPhotoDetails.as_view()),
]