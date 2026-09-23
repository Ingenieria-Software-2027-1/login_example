from django.urls import path

from . import views

app_name = "spaces"

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("crear/", views.crear_espacio, name="crear"),
]