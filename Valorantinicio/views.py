from logging import info
from django.shortcuts import render
from .forms import CrearProfesionalesForm, JugadoresvalorantForm
from Valorantinicio.models import Profesionales
from Valorantinicio.models import jugadoresvalorant
from Valorantinicio.forms import BuscarJugadorForm
from Valorantinicio.forms import ModificarProfesionalesForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# importaciones de CBV
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin

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
    form = JugadoresvalorantForm()

    if request.method == 'POST':
        form = JugadoresvalorantForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jugador = jugadoresvalorant(
                nombre=info['nombre'],
                equipo=info['equipo'],
                rol=info['rol'],
                nacionalidad=info['nacionalidad'],
                edad=info['edad']
            )
            jugador.save()
            segmensaje = f'Se creó el jugador {jugador.nombre}'
        else:
            return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form})

    return render(request, 'Valorantinicio/Jugadoresvalorant.html', {'form': form, 'segmensaje': segmensaje})

@login_required
def buscar_jugador_view(request):
    if request.method == 'POST':
       form = BuscarJugadorForm(request.POST)
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

# CRUD Y CBV (COMENTADAS POR QUE GENERABAN ERRORES DEBIDO A QUE AVANZE MUCHO EN EL TRABAJO Y AL NUNCA HABER HECHO LA LISTA PRINCIPAL NO PUDE COLOCAR CADA VIEW, URL, ETC, EN SU LUGAR POR ENDE Y DEBIDO A LA FALTA DE TIEMPO NO LO PUDE CORREGIR Y TUVE QUE DEJAR TODO LO RELACIONADO AL CRUD Y CBV COMO COMENTADO)


# def Eliminar_Profesionales(request, Profesionales_id):
 
#    profesionales = Profesionales.objects.get(id=Profesionales_id)
#    profesionales.delete()

#    return redirect('Valorantinicio: Crear_Profesionales')

# def Modificar_Profesionales(request, Profesionales_id):
#      profesionales_a_modificar = Profesionales.objects.get(id=Profesionales_id)

#      if request.method == 'POST':
#          form = ModificarProfesionalesForm(request.POST)
#          if form.is_valid():
#              info = form.cleaned_data
#              profesionales_a_modificar.nombre = inicio['nombre']
#              profesionales_a_modificar.edad = inicio['edad']
#              profesionales_a_modificar.save()
#              return redirect('Valorantinicio: Crear_Profesionales')

#          else:
#              return render(request, 'Valorantinicio/Modificar_Profesionales.html', {'form':form})
    
#      form = ModificarProfesionalesForm(initial={'nombre': profesionales_a_modificar.nombre,'edad': profesionales_a_modificar.edad})
#      return render(request, 'Valorantinicio/Modificar_Profesionales.html', {'form':form})

# class CrearProfesionales(CreateView, LoginRequiredMixin):
#     model = Profesionales
#     template_name = 'Valorantinicio/CBV/Crear_Profesionales_CBV.html'
#     fields = ['nombre', 'edad', 'descripcion']
#     success_url = reverse_lazy('Valorantinicio:Crear_Profesionales_CBV')

# class ListarProfesionales(Listview, LoginRequiredMixin):
#     model = Profesionales
#     template_name = 'Valorantinicio/CBV/Listar_Profesionales_CBV.html'
#     context_object_name = 'Profesionales'

# class ModificarProfesionales(UpdateView, LoginRequiredMixin):
#     model = Profesionales
#     template_name = 'Valorantinicio/CBV/Modificar_Profesionales_CBV.html'
#     fields = ['nombre', 'edad', 'descripcion']
#     succes_url = reverse_lazy('Valorantinicio:Listar_Profesionales')

# class EliminarProfesionales(DeleteView, LoginRequiredMixin):
#     model = Profesionales
#     template_name = 'Valorantinicio/CBV/Eliminar_Profesionales_CBV.html'
#     succes_url = reverse_lazy('Valorantinicio:Listar_Profesionales')

# class MostrarProfesionales(DetailView, LoginRequiredMixin):
#     model = Profesionales
#     template_name = "Valorantinicio/CBV/Mostrar_Profesionales_CBV.html"

