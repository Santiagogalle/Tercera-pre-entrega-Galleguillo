from django.urls import path
from ValoUsers import views
from django.contrib.auth.views import LogoutView

app_name = 'ValoUsers'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('logout/', LogoutView.as_view(template_name='ValoUsers/logout.html'), name='logout'),
]
