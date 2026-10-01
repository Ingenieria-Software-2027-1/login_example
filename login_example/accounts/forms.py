from django.contrib.auth.forms import AuthenticationForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Correo Electronico', 
        
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'ejemplo@dominio.com',
                'autofocus': True 
            }
        )
    )
    
    def clean(self):
        self.cleaned_data = super().clean()
        
        return self.cleaned_data
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electronico')
    
    class Meta:
        model = CustomUser
        
        fields = ('username', 'email', 'is_renter', 'is_host')