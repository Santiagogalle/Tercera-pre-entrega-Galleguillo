from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def login(request):

#    if request.method == 'POST':
#       form = AuthenticationForm(request.POST)
#       if form.is_valid():
#         usuario = form.cleaned_data['username']
#         contrasenia = form.cleaned_data['password']

#         user = authenticate(username=usuario, password=contrasenia)

#         django_login(request, user)
#         return redirect('Valorantinicio:Valorantinicio')
       
#       else:
#        return render(request, 'ValoUsers/login.html', {'form': form})

#    form = AuthenticationForm()
#    return render(request, 'ValoUsers/login.html', {'form': form})

def login(request):
  if request.method == "POST":
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
      django_login(request, user)
      return redirect("Valorantinicio:Valorantinicio")
    else:
      return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
  else:
    form = AuthenticationForm()
    return render(request, 'ValoUsers/login.html', {'form':form})
  

# def registro(request):

#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('ValoUsers:login')
#     else:
#       return render(request, 'ValoUsers/registro.html', {'form':form})

#   form = UserCreationForm()
#   return render(request, 'ValoUsers/registro.html', {'form':form})

# def registro(request):
#     if request.method == "POST":
#         userCreate = UserCreationForm(request.POST)
#         if userCreate is not None:
#             userCreate.save()
#             return redirect('login')
#     else:
#         return render(request, 'registro.html')

def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate.is_valid():  # Verificar si el formulario es válido
            userCreate.save()
            return redirect('ValoUsers:login')
    else:
        userCreate = UserCreationForm()  # Instanciar el formulario vacío para mostrarlo en la página
    return render(request, 'ValoUsers/registro.html', {'form': userCreate})