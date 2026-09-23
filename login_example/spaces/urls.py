from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_espacio, name='crear_espacio'),
    path('catalogo/', views.catalogo, name='catalogo'),
]