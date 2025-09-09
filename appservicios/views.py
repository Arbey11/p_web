from django.shortcuts import render
from appservicios.models import Servicios

# Create your views here.

def servicios(request):
    serv = Servicios.objects.all() # que importe todos los objetos de la clase Servicio 
    return render(request, "appservicios/servicios.html", {'servicio':serv})    