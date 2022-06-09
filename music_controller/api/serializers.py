# take the model that has the python code and translate it to json response
from rest_framework import serializers
from .models import Room

# class for this roomserializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # model to serialize
        model = Room
        # fields to serialize i.e give to us
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at') # id is the primary key is a unique key to identify the model in relation to the others
