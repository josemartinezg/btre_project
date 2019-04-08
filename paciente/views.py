from django.shortcuts import render
from .models import Paciente
#Pasaremos datos del modelo desde un diccionario.
def index(request):
    #Trayendo "Listings" desde la DB:
    paciente = Paciente.objects.all()
    context = {
        'paciente': paciente
    }
    return render(request, 'paciente/paciente.html')

def paciente(request):
    return render(request, 'paciente/paciente.html')

def search(request):
    return render(request, 'paciente/paciente.html')
