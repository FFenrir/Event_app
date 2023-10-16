from django.shortcuts import render
from .models import Event
from rest_framework import generics
from .serializers import EventSerializer

# Create your views here.


class EventListView(generics.ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer