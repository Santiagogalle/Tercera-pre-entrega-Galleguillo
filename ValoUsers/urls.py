from django.urls import path
from ValoUsers import views

app_name = 'ValoUsers'

urlpatterns = [
   path('login/', views.login, name='login') 
]
