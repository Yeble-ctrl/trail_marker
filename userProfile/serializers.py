from userProfile.models import Profile, Qualification, WorkExperience, skills
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ['user']
    def create(self, validated_data):
        return Qualification.objects.create(**validated_data)

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        exclude = ['user']
    def create(self, validated_data):
        return WorkExperience.objects.create(**validated_data)

class skillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = skills
        exclude = ['user']
    def create(self, validated_data):
        return skills.objects.create(**validated_data)