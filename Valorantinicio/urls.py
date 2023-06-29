from django.urls import path
from Valorantinicio import views

app_name = 'Valorantinicio'

urlpatterns = [
    path('', views.inicio, name='Valorantinicio'),
    path('Profesionales/Crear/', views.inicio, name='Crear_Profesionales'),
    path('Jugadores/valorant/', views.inicio, name='Jugadoresvalorant'),
    ]
