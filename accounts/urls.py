from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.GetUsers.as_view()),
    path('register/', views.RegisterUser.as_view()),
    path('getUsers/', views.GetUsers.as_view()),
    path('userDetails/<str:username>/', views.UserDetails.as_view())
]
