from django.urls import path
from Valorantinicio import views

urlpatterns = [
    path('', views.inicio, name='Valorantinicio')
]
