from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwnerOrReadOnly
from accounts.serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserSerializer

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

class UserDetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)