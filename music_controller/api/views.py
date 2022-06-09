from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# Create your views here.

# get the view setup
class RoomView(generics.ListAPIView):
    # to get all the of the Room objects
    queryset = Room.objects.all()
    # the serializer class to use from ./seriaizers.py
    serializer_class = RoomSerializer