from django.contrib.auth.models import User
from userProfile.models import Profile, Qualification, WorkExperience, skills as Skill
from userProfile.serializers import ProfileSerializer, QualificationSerializer, WorkExperienceSerializer, skillsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from userProfile.permissions import IsOwnerOrReadOnly

# Generic views for the Profile model
class Profiles(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Profile.objects.all()
        username = self.request.query_params.get('username')
        user = User.objects.get(username = username)
        if username is not None:
            queryset = queryset.filter(user = user)
        return queryset

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    
    def get_object(self):
        user = self.request.user
        return Profile.objects.get(user = user)

# Generic views for the Qualifications model
class Qualifications(generics.ListCreateAPIView):
    permisson_classes = [IsAuthenticated]
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QualificationDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = QualificationSerializer

    def get_object(self):
        user = self.request.user
        return Qualification.objects.get(user = user)

# Generic views for the work experience model
class WorkExperiences(generics.ListCreateAPIView):
    permisson_classes = [IsAuthenticated]
    serializer_class = WorkExperienceSerializer
    queryset = WorkExperience.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkExperienceDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = WorkExperienceSerializer

    def get_object(self):
        user = self.request.user
        return WorkExperience.objects.get(user = user)

# Generic views for the skills model
class Skills(generics.ListCreateAPIView):
    permisson_classes = [IsAuthenticated]
    serializer_class = skillsSerializer
    queryset = Skill.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class skillsDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = skillsSerializer

    def get_object(self):
        user = self.request.user
        return Skill.objects.get(user = user)
