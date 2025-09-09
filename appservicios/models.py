from django.db import models

# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='media_servicios')
    creado = models.DateTimeField(auto_now_add=True) # para que lo haga automaticamente
    actualizado = models.DateTimeField(auto_now_add=True)