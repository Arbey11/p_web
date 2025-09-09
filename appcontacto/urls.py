from django.urls import path
from appcontacto.views import contacto, respuesta_contacto

urlpatterns = [
    path('contacto/', contacto),  # Ruta base del blog
    path('contacto/respuesta_contacto/', respuesta_contacto),
]

