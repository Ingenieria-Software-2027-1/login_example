from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import EmailAuthenticationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True # Si ya estoy logueado, no me dejes ver de nuevo el login
    

def dashboard_view(request):
    usuario_actual = request.user 
    
    if usuario_actual.is_host:
        # Es alguien que quiere poner espacios en renta
        return render(request, 'accounts/host_home.html')
    
    elif usuario_actual.is_renter:
        # Es alguien que buscar rentar un espacio
        return render(request, 'accounts/renter_home.html')
    
    else:
        # Por si el usuario es superusuario
        return render(request, 'accounts/admin_home.html')
    
class RegistroView(CreateView):
    template_name = 'accounts/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')