from django.db import models

# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6, default="ffffff")
    
class Stats(models.Model):
    hp = models.SmallIntegerField()
    atk = models.SmallIntegerField()
    dfn = models.SmallIntegerField()
    spatk = models.SmallIntegerField()
    spdef = models.SmallIntegerField()
    spd = models.SmallIntegerField()

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    generation = models.SmallIntegerField()
    types = models.ManyToManyField(Types)
    stats = models.ManyToManyField(Stats)

