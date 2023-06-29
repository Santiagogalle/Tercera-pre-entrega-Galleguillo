from django import forms

class CrearProfesionalesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(null=True)


class JugadoresvalorantForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    equipo = forms.CharField(max_length=100)
    rol = forms.ChoiceField(choices=[('Duelista', 'Duelista'), ('Controlador', 'Controlador'), ('Iniciador', 'Iniciador'), ('Centinela', 'Centinela')])
    nacionalidad = forms.CharField(max_length=100)
    edad = forms.IntegerField(min_value=0, max_value=150)
