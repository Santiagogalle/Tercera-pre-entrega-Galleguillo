from django.shortcuts import render
from .forms import CrearProfesionalesForm, JugadoresvalorantForm
from Valorantinicio.models import Profesionales
from Valorantinicio.models import jugadoresvalorant
from Valorantinicio.forms import BuscarJugadorForm

# Create your views here.

def inicio(request):

    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/Valorantinicio.html', {'form' : form})

def crear_Profesionales(request):
    mensaje = ''

    if request.method == 'POST':
      form = CrearProfesionalesForm(request.POST)
      if form.is_valid():
         info = form.cleaned_data
         profesionales = Profesionales(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])
         profesionales.save()
         mensaje = f'se creo el profesional {profesionales.nombre}'
      
      else:
       return render(request, 'Valorantinicio/crear_Profesionales.html', {'form': form})

    form = CrearProfesionalesForm()
    return render(request, 'Valorantinicio/crear_Profesionales.html', {'form': form, 'mensaje': mensaje})

def Jugadores_valorant(request):
    segmensaje = ''

    if request.method == 'POST':
       form = JugadoresvalorantForm()
       if form.is_valid():
          info = form.cleaned_data
          Jugadoresvalorant = jugadoresvalorant(nombre=info['nombre'],equipo=info['equipo'],rol=info['rol'],nacionalidad=info['nacionalidad'],edad=info['edad'])
          Jugadoresvalorant.save()
          segmensaje = f'se creo el jugador {Jugadoresvalorant.nombre}'

       else:
          return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})


    form = JugadoresvalorantForm()
    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form, 'mensaje': segmensaje})

def buscar_jugador_view(request):

    form = BuscarJugadorForm(request.GET)
    if form.is_valid():
        nombre_jugador = form.cleaned_data['nombre_jugador']
        # Realizar la búsqueda en la base de datos y obtener los resultados
        resultados = jugadoresvalorant.objects.filter(nombre__icontains=nombre_jugador)
        # Pasar los resultados al contexto para mostrarlos en la plantilla
    else:
        resultados = None

    context = {'form': form, 'resultados': resultados}
    return render(request, 'buscar_jugador.html', context)
