from django.db import models
from pokedex.models import Pokemon
from pokedex.models import Types

# Create your models here.
class Team(models.Model):
    teamPKMN = models.ManyToManyField(Pokemon)