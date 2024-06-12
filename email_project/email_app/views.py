from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    send_mail(
        'Saludo desde Django',
        'Hola Mundo!!',
        'victorgonzalomaldonadovilca@gmail.com',
        ['vmaldonadov@unsa.edu.pe'],
    )
    return render(request, "email/index.html")