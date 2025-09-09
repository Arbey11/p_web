from django.urls import path
from apphome.views import home, tienda

urlpatterns = [
    path('home/', home),
    path('tienda/', tienda),
] 

 