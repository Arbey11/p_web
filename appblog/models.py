from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
 

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='media_blog', null=True, blank=True) # Cuando subo una imagen, guárdala en una carpeta media_servicios
    relacion_categorias = models.ManyToManyField(Categorias) # me relaciona si un post tiene varias vategorias
    creado = models.DateTimeField(auto_now_add=True) # para que lo haga automaticamente
    actualizado = models.DateTimeField(auto_now_add=True) 

    