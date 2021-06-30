from django.db import models

# Create your models here.

class Movie(models.Model):
    #def __init__(self, id, name, director):
    #    self.id = id
    #    self.name = name
    #    self.director = director
    id = models.IntegerField(primary_key = True, blank = False)
    name = models.CharField(max_length = 15, blank = False)
    director = models.CharField(max_length= 15, blank= False)

class Songs(models.Model):
    name = models.CharField(max_length = 15, blank = False)
    duration = models.PositiveIntegerField(blank = False)