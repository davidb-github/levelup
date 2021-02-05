from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import GameType
from django.contrib.auth.models import Gamer

class Game(models.Model):
    
    title     = models.CharField(max_length=50)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)