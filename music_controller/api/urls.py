from django.urls import path
from .views import *

# /api/room contains the view of the Room model

urlpatterns = [
    path('room', RoomView.as_view(), name='index'),
]