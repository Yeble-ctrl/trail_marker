from django.urls import path
from userProfile import views

urlpatterns = [
    # Profile views URL patterns
    path('profiles/', views.Profiles.as_view()),  # Handles both create and list
    path('profile-details/', views.ProfileDetails.as_view()),

    # Qualification views URL patterns
    path('qualifications/', views.Qualifications.as_view()),  # Handles both create and list
    path('qualification-details/', views.QualificationDetails.as_view()),

    # WorkExperience views URL patterns
    path('work-experiences/', views.WorkExperiences.as_view()),  # Handles both create and list
    path('work-experience-details/', views.WorkExperienceDetails.as_view()),

    # Skill views URL patterns
    path('skills/', views.Skills.as_view()),  # Handles both create and list
    path('skill-details/', views.skillsDetails.as_view()),
]