from django.urls import path 
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # ruta para iniciar sesion
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # ruta para cerrar sesion
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Ruta para el panel dinamico
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Ruta para registrar usuario
    path('registro/', views.RegistroView.as_view(), name='registro'),
]