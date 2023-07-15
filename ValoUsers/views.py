from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):

   if request.method == 'POST':
      if form.is_valid():
         ...
      else:
       return render(request, 'ValoUsers/login.html', {'form': form})


   form = AuthenticationForm()
   return render(request, 'ValoUsers/login.html', {'form': form})