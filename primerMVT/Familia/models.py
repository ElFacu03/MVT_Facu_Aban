from django.db import models
import datetime

# Create your models here.
class Tio(models.Model):
    
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    cumple=models.DateField()

class Primo(models.Model):
   
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    cumple=models.DateField()

class Abuelo(models.Model):
    
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    cumple=models.DateField()