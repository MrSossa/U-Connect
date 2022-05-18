from pickletools import long1
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Register(models.Model):
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
    Owner = models.CharField(default="",max_length=50)
    route = models.JSONField(null=True, blank=True)
    startdate = models.DateField(default=timezone.now)
    startTime = models.TimeField(default=timezone.now)
    description = models.CharField(max_length=500,default="")
    petfriendly = models.BooleanField(default=False)
    state = models.BooleanField(default=True)
    participants = models.JSONField(null=True, blank=True)
    def data(self):
        return [self.route,self.Owner,self.startdate,self.description,self.petfriendly,self.id]
