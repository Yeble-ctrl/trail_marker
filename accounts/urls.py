from django.urls import path
from accounts import views

urlpatterns = [
    path('users/', views.Users.as_view()),
    path('users/<str:username>/', views.UserDetails.as_view()),
]
