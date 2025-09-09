from django.contrib import admin
from appservicios.models import Servicios

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display = ('titulo', 'contenido', 'imagen', 'creado', 'actualizado')

admin.site.register(Servicios, ServiciosAdmin) 