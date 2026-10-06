from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Space
from .forms import SpaceForm

@login_required
def crear_espacio(request):
    """
    Vista de creación (Solo Anfitriones): Protegida para usuarios logueados.
    Verifica rol y asigna automáticamente el anfitrión actual.
    """
    # Se evalúa el rol de anfitrión (compatible con diferentes estructuras de usuario del proyecto)
    is_host = getattr(request.user, 'is_host', False) or getattr(request.user, 'role', '') == 'host' or request.user.is_superuser

    if not is_host:
        messages.error(request, "Acceso denegado: Se requieren permisos de Anfitrión para registrar espacios.")
        return redirect('catalogo_espacios')

    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            space = form.save(commit=False)
            space.host = request.user  # Asigna automáticamente el anfitrión actual
            space.save()
            messages.success(request, f"¡El espacio '{space.name}' ha sido publicado con éxito!")
            return redirect('catalogo_espacios')
    else:
        form = SpaceForm()

    return render(request, 'spaces/crear_espacios.html', {'form': form})


@login_required
def catalogo_espacios(request):
    """
    Vista de catálogo (Arrendatarios): Consulta la BD usando el ORM
    para traer todos los espacios disponibles y enviarlos como contexto.
    """
    espacios = Space.objects.all().order_by('-created_at')
    return render(request, 'spaces/catalogo.html', {'espacios': espacios})