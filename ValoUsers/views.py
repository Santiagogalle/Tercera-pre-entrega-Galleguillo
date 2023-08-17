from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
# from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from ValoUsers.forms import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDeUsuario
from django.urls import reverse_lazy
from ValoUsers.models import InfoExtra

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

# def login(request):
#    if request.method == "POST":
#      user = authenticate(username=request.POST['user'], password=request.POST['password'])
#      if user is not None:
#        django_login(request, user)

#        InfoExtra.objects.get_or_create(user=user)
      
#        return redirect("Valorantinicio:Valorantinicio")
#      else:
#        return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
#    else:
#      form = AuthenticationForm()
#      return render(request, 'ValoUsers/login.html', {'form':form})
   
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)

            InfoExtra.objects.get_or_create(user=user)

            return redirect("Valorantinicio:Valorantinicio")
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'ValoUsers/login.html', {'form': form})

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)

#             InfoExtra.objects.get_or_create(user=user)

#             return redirect("Valorantinicio:Valorantinicio")
#         else:
#             return render(request, 'login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})
  

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
        userCreate = MiFormularioDeCreacionDeUsuarios(request.POST)
        if userCreate.is_valid():  # Verificar si el formulario es válido
            userCreate.save()
            return redirect('ValoUsers:login')
    else:
        userCreate = MiFormularioDeCreacionDeUsuarios()  # Instanciar el formulario vacío para mostrarlo en la página
    return render(request, 'ValoUsers/registro.html', {'form': userCreate})

@login_required
def edicion_perfil(request):
  info_extra_user = request.user.infoextra
  if request.method == 'POST':
    form = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, request.FILES, instance=request.user)
    if form.is_valid():

      avatar = form.cleaned_data.get('avatar')
      if avatar:
       info_extra_user.avatar = avatar
       info_extra_user.save()

      form.save()
      return redirect('Valorantinicio:Valorantinicio')
  else:
     form = MiFormularioDeEdicionDeDatosDeUsuario(initial={'avatar': info_extra_user.avatar}, instance=request.user)
  
  return render(request, 'ValoUsers/edicion_perfil.html', {'form':form})

class ModificarPass(LoginRequiredMixin, PasswordChangeView):
   template_name = 'ValoUsers/modificar_pass.html'
   success_url = reverse_lazy('ValoUsers:editar_perfil')