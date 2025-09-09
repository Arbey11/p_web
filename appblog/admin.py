from django.contrib import admin
from appblog.models import Categorias, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display = ('titulo', 'contenido')
    
admin.site.register(Categorias, CategoriaAdmin) 
admin.site.register(Post, PostAdmin) 