from pickletools import long1
from django.db import models

# Create your models here.
class Logo(models.Model):
    image = models.ImageField(upload_to='Logo/images/')
    url = models.URLField(blank=True)

class NavBar(models.Model):
    url = models.URLField(blank=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    image = models.ImageField(upload_to='User/images/')
    url = models.URLField(blank=True)

class Car(models.Model):
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Placa = models.CharField(max_length=6)
    color = models.CharField(max_length=20)
    url = models.URLField(blank=True)

class Route(models.Model):
    lat1 = models.FloatField()
    long1 = models.FloatField()
    lat2 = models.FloatField()
    long2 = models.FloatField()
    def data(self):
        return [self.lat1,self.long1,self.lat2,self.long2]