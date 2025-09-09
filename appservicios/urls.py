from django.urls import path
from appservicios.views import servicios

urlpatterns = [
    path('servicios/', servicios),
] 
   
