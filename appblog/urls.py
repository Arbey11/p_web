from django.urls import path
from appblog.views import blog, categoria

urlpatterns = [
    path('blog/', blog),  # Ruta base del blog
    path('blog/categoria/<int:categorias_id>/', categoria),  # Ruta para categoría con parámetro entero
]

