from django.urls import path
from ValoUsers import views
from django.contrib.auth.views import LogoutView

app_name = 'ValoUsers'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('logout/', LogoutView.as_view(template_name='ValoUsers/logout.html'), name='logout'),
   path('registro/', views.registro, name='registro'),
   path('perfil/editar/', views.edicion_perfil, name='editar_perfil'),
   path('perfil/editar/password', views.ModificarPass.as_view(), name='modificar_pass'),
   path('info/user', views.user_view, name='user_info'),
   path('extra/user', views.extra_view, name='extra user info')
]

