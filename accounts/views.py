from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.permissions import IsOwnerOrReadOnly
from accounts.serializers import UserSerializer

class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        # Apply IsAuthenticated permission only to the list method
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)  # Explicitly check permissions

        # Use the default list behavior
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UserSerializer