from userProfile.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Profile
        exclude = ['user']

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)