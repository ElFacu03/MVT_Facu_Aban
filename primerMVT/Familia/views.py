from django.http import HttpResponse
from django.shortcuts import render
from .models import Tio, Primo, Abuelo
from django.template import loader

# Create your views here.
def tio(request, nombre, edad, cumple):

    diccionario = {"nombre":nombre, "edad":edad, "cumple":cumple}   
    tio_tia = Tio(nombre=nombre, edad=edad, cumple=cumple)
    tio_tia.save()    

    plantilla = loader.get_template("tio.html")
    
    return HttpResponse (plantilla.render(diccionario))

def primo(request, nombre, edad, cumple):
    
    diccionario = {"nombre":nombre, "edad":edad, "cumple":cumple}
    primos = Primo(nombre=nombre, edad=edad, cumple=cumple)
    primos.save()

    plantilla = loader.get_template("primo.html")
    
    return HttpResponse (plantilla.render(diccionario))

def abuelo(request, nombre, edad, cumple):
    
    diccionario = {"nombre":nombre, "edad":edad, "cumple":cumple}
    abuelos = Abuelo(nombre=nombre, edad=edad, cumple=cumple)
    abuelos.save()

    plantilla = loader.get_template("abuelo.html")
    
    return HttpResponse (plantilla.render(diccionario))

