from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'Valorantinicio/Valorantinicio.html')

def crear_Profesionales(request):
    return render(request, 'Valorantinicio/crear_Profesionales.html')

from django.shortcuts import render
from .forms import CrearProfesionalesForm

def crear_profesionales(request):
    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/crear_Profesionales.html', {'form': form})


from django.shortcuts import render
from .forms import JugadoresvalorantForm

def crear_profesionales(request):
    form = JugadoresvalorantForm()
    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})