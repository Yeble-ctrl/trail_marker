from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.GetUsers.as_view()),
    path('register/', views.RegisterUser.as_view())
]
