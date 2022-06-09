from django.urls import path
from .views import *

urlpatterns = [
    path('room', RoomView.as_view(), name='index'),
]