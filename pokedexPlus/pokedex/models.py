from django.db import models

# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6, default="ffffff")

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    # generation = models.SmallIntegerField()
    hp = models.SmallIntegerField()
    atk = models.SmallIntegerField()
    dfn = models.SmallIntegerField()
    spatk = models.SmallIntegerField()
    spdef = models.SmallIntegerField()
    spd = models.SmallIntegerField()
    types = models.ManyToManyField(Types)
    image = models.CharField()
    
    def __str__(self):
        return self.name

