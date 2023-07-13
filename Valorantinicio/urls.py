from django.urls import path
from Valorantinicio import views

app_name = 'Valorantinicio'

urlpatterns = [
    path('', views.inicio, name='Valorantinicio'),
    path('Profesionales/Crear/', views.crear_Profesionales, name='Crear_Profesionales'),
    path('Profesionales/Eliminar/', views.Eliminar_Profesionales, name='Eliminar_Profesionales'),
    path('Jugadores/valorant/', views.Jugadores_valorant, name='Jugadoresvalorant'),
    ]
