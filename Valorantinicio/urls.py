from django.urls import path
from Valorantinicio import views

app_name = 'Valorantinicio'

urlpatterns = [
    path('', views.inicio, name='Valorantinicio'),
    path('Profesionales/Crear/', views.crear_Profesionales, name='Crear_Profesionales'),
    path('Profesionales/Eliminar/<int:Profesionales_id>/', views.Eliminar_Profesionales, name='Eliminar_Profesionales'),
    path('Jugadores/valorant/', views.Jugadores_valorant, name='Jugadoresvalorant'),
    path('Profesionales/Modificar/<int:Profesionales_id>/', views.Modificar_Profesionales, name='Modificar_Profesionales'),

    #CBV
    # path('Profesionales/Crear/', views.CreateView.as_view(), name='Crear_Profesionales'),

]

