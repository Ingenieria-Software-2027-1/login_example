from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SpaceForm
from .models import Space

@login_required(login_url="login")
def crear_espacio(request):
    if not request.user.is_host:
        return redirect("dashboard")

    if request.method == "POST":
        form = SpaceForm(request.POST)

        if form.is_valid():
            espacio = form.save(commit=False)
            espacio.anfitrion = request.user
            espacio.save()

            messages.success(request, "el espacio se publico bien")
            return redirect("spaces:crear")
    else:
        form = SpaceForm()

    return render(request, "spaces/crear_espacio.html", {"form": form})

@login_required(login_url="login")
def catalogo(request):
    if not request.user.is_renter:
        return redirect("dashboard")

    espacios = Space.objects.filter(disponible=True).order_by("-creado_en")
    return render(request, "spaces/catalogo.html", {"espacios": espacios})