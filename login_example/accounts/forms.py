from django.contrib.auth.forms import AuthenticationForm
from django import forms 

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