from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):
    return render(request, "appcontacto/contacto.html") 

# enviando la informacion al correo:

def respuesta_contacto(request):
    if request.method == 'POST':
        subject = request.POST['asunto']
        message = f"{request.POST['mensaje']}\n\nEmail de contacto: {request.POST['email']}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['didier.garcia.galviz@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'AppContacto/respuesta_form.html')
    return render(request, 'AppContacto/contacto.html')  