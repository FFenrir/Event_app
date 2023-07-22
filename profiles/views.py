from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer, ProfileRegistrationSerializer
from rest_framework import generics

# Create your views here.

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile
    serializer_class = ProfileSerializer    


class ProfileRegistrationView(generics.CreateAPIView):
    serializer_class = ProfileRegistrationSerializer