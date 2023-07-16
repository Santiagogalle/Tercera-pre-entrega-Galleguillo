from django.urls import path
from Valorantinicio import views

app_name = 'Valorantinicio'

urlpatterns = [
    path('', views.inicio, name='Valorantinicio'),
    path('Profesionales/Crear/', views.crear_Profesionales, name='Crear_Profesionales'),
    # path('Profesionales/Eliminar/<int:Profesionales_id>/', views.Eliminar_Profesionales, name='Eliminar_Profesionales'),
    path('Jugadores/valorant/', views.Jugadores_valorant, name='Jugadoresvalorant'),
    # path('Profesionales/Modificar/<int:Profesionales_id>/', views.Modificar_Profesionales, name='Modificar_Profesionales'),
    path('about/', views.about_view, name='aboutme'),

    # #CBV
    # # path('Profesionales/Crear/', views.CreateView.as_view(), name='Crear_Profesionales'),
    #  path('Profesionales/Eliminar/<int:pk>/', views.Eliminar_Profesionales.as_view(), name='Eliminar_Profesionales'),
    #  path('Profesionales/Modificar/<int:pk>/', views.Modificar_Profesionales.as_view(), name='Modificar_Profesionales'),
    #  path('Profesionales/', views.ListarProfesionales.as_view(), name='Listar_Profesionales')
    #  path('Profesionales/<int:pk>/', views.Mostrar_Profesionales.as_view(), name='Mostrar_Profesionales'),
]

