from django.urls import path
from userProfile import views

urlpatterns = [
    path('createProfile/', views.createProfile.as_view()),
    path('getProfiles/', views.GetProfiles.as_view()),
    path('profileDetails/<int:pk>/', views.ProfileDetails.as_view()),
]
