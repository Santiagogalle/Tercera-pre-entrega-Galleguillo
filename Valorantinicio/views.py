from django.shortcuts import render
from .forms import CrearProfesionalesForm, JugadoresvalorantForm

# Create your views here.

def inicio(request):

    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/Valorantinicio.html', {'form' : form})

def crear_Profesionales(request):
    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/crearProfesionales.html', {'form': form})

def Jugadores_valorant(request):
    form = JugadoresvalorantForm()
    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})