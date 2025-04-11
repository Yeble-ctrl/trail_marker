from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]) # Validate that the username is unique

    password = serializers.CharField(write_only=True) # Hide password in serialized data
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)