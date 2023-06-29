from django.shortcuts import render
from .forms import CrearProfesionalesForm

# Create your views here.

def inicio(request):

    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/Valorantinicio.html', {'form' : form})

def crear_profesionales(request):
    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/crearProfesionales.html', {'form': form})

from django.shortcuts import render
from .forms import JugadoresvalorantForm

def crear_profesionales(request):
    form = JugadoresvalorantForm()
    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})