from django.db import models
import string
import random

# function to generate the randome code
def generate_unique_code():
    # set a length for the code
    length = 6
    # loop
    while True:
        # generate random code
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # check if any of the codes is already in use, if not then return it
        if Room.objects.filter(code=code).count() == 0:
            # break out of the loop
            break
    # return the code
    return code

# Create your models here.
class Room(models.Model):
    # code to identiy the room
    code = models.CharField(max_length=8, default="", unique=True)
    # host tracker sort of that links to the host
    host = models.CharField(max_length=50, unique=True)
    # can guests pause which is no
    guest_can_pause = models.BooleanField(null=False, default=False)
    # vottes: the votes for skiping the song
    votes_to_skip = models.IntegerField(null=False, default=1)
    # created at  i.e date adn time
    created_at = models.DateTimeField(auto_now_add=True)

# you would want to return json values for the front end to easily parse