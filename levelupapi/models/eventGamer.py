from django.db import models
from django.contrib.auth.models import Event
from django.contrib.auth.models import Gamer

class eventGamer(models.Model):
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)