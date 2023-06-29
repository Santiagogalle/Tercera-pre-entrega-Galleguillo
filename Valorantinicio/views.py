from django.shortcuts import render
from .forms import CrearProfesionalesForm

# Create your views here.

def inicio(request):
    return render(request, 'Valorantinicio/Valorantinicio.html')

def crear_profesionales(request):
    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/crear_Profesionales.html', {'form': form})

from django.shortcuts import render
from .forms import JugadoresvalorantForm

def crear_profesionales(request):
    form = JugadoresvalorantForm()
    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})