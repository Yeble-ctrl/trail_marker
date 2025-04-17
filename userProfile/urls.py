from django.urls import path
from userProfile import views

urlpatterns = [
    # Profile views url patterns
    path('createProfile/', views.createProfile.as_view()),
    path('getProfiles/', views.GetProfiles.as_view()),
    path('profileDetails/', views.ProfileDetails.as_view()),

    # Qualification views url patterns
    path('qualification/', views.Qualifications.as_view()),
    path('qualificationDetails/', views.QualificationDetails.as_view()),

    # WorkExperience views url patterns
    path('WorkExperience/', views.WorkExperiences.as_view()),
    path('WorkExperienceDetails/', views.WorkExperienceDetails.as_view()),

    # skill views url patterns
    path('skill/', views.GetCreateSkills.as_view()),
    path('skillDetails/', views.skillsDetails.as_view()),
]