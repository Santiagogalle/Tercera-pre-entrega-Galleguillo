from django.db import models

# Create your models here.

class Profesionales(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)

    def _str_(self):
        return self.nombre
    
class jugadoresvalorant(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    rol = models.CharField(choices=[('Duelista', 'Duelista'), ('Controlador', 'Controlador'), ('Iniciador', 'Iniciador'), ('Centinela', 'Centinela')], max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()

    def _str_(self):
        return self.nombre