from django.db import models

# Create your models here.

class Profesionales(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    
class Jugadoresvalorant(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    rol = models.ChoiceField(choices=[('Duelista', 'Duelista'), ('Controlador', 'Controlador'), ('Iniciador', 'Iniciador'), ('Centinela', 'Centinela')])
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField(min_value=0, max_value=150)