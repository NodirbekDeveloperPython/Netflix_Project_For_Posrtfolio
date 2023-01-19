from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Aktyor(models.Model):
    ism = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50, blank=True)
    jins = models.CharField(max_length=50, blank=True)
    tugilgan_yil = models.DateField(null=True)
    def __str__(self): return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    yil = models.DateField(null=True)
    reyting = models.FloatField()
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self): return self.nom

class Comment(models.Model):
    izoh = models.CharField(max_length=300)
    sana = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    def __str__(self): return self.izoh