from django.urls import path
from Valorantinicio import views

app_name = 'Valorantinicio'

urlpatterns = [
    path('', views.inicio, name='Valorantinicio'),
    path('Profesionales/crear/', views.inicio, name='crear_Profesionales'),
    ]
