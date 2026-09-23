from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SpaceForm
from .models import Space

@login_required
def crear_espacio(request):
    if not request.user.is_host:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            espacio = form.save(commit=False)
            espacio.host = request.user
            espacio.save()
            return redirect('dashboard')
    else:
        form = SpaceForm()

    return render(request, 'spaces/crear_espacio.html', {'form': form})


def catalogo(request):
    espacios = Space.objects.filter(is_available=True)
    return render(request, 'spaces/catalogo.html', {'espacios': espacios})

# Create your views here.
