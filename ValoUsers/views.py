from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

# Create your views here.

def login(request):

   if request.method == 'POST':
      if form.is_valid():
        usuario = form.cleaned_data['username']
        contrasenia = form.cleaned_data['password']

        user = authenticate(username=usuario, password=contrasenia)

        django_login(request, user)
        return redirect('Valorantinicio:Valorantinicio')
       
      else:
       return render(request, 'ValoUsers/login.html', {'form': form})

   form = AuthenticationForm()
   return render(request, 'ValoUsers/login.html', {'form': form})