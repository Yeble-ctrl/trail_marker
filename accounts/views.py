from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer