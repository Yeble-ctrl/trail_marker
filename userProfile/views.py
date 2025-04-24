from django.contrib.auth.models import User
from userProfile.models import Profile, Qualification, WorkExperience, skills as Skill
from userProfile.serializers import ProfileSerializer, QualificationSerializer, WorkExperienceSerializer, skillsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from userProfile.permissions import IsOwnerOrReadOnly
from django.http import Http404

# Generic views for the Profile model
class Profiles(generics.ListCreateAPIView):
    """
    View for Post and Get requests
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name')
        queryset = Profile.objects.all()
        if first_name is not None:
            user = User.objects.get(first_name = first_name)
            if user is not None:
                queryset = queryset.filter(user = user)
        return queryset

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        return get_user_object(self, Profile)
        # username = self.request.query_params.get('username')
        # if username is not None:
        #     profile = get_user_object(username, Profile)
        #     self.check_object_permissions(self.request, profile)
        #     return profile
        # return Profile.objects.get(user = self.request.user)

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
        return get_user_object(self, Qualification)

        # username = self.request.query_params.get('username')
        # if username is not None:
        #     qualification = get_user_object(username, Qualification)
        #     self.check_object_permissions(self.request, qualification)
        #     return qualification
        # return Qualification.objects.get(user = self.request.user)

# Generic views for the work experience model
class WorkExperiences(generics.ListCreateAPIView):
    permisson_classes = [IsAuthenticated]
    serializer_class = WorkExperienceSerializer
    queryset = WorkExperience.objects.all()

class WorkExperienceDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = WorkExperienceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        return get_user_object(self, WorkExperience)

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
        return get_user_object(self, Skill)
        
def get_user_object(view, model):
    """
    Generic function to get an object based on the username.
    :param username: The username of the user.
    :param model: The model to query.
    :return: The object if found, otherwise raises Http404.
    """
    username = view.request.query_params.get('username')
    if username is not None:
        user = User.objects.get(username=username)
        if user is not None:
            obj = model.objects.get(user=user)
            if obj is not None:
                view.check_object_permissions(view.request, model)
                return obj
            raise Http404(f"{model.__name__} does not exist for the user")
        raise Http404("User does not exist")
    return model.objects.get(user = view.request.user)