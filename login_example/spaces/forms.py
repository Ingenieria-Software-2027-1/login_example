from django import forms
from .models import Space

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'description', 'capacity', 'price_per_hour']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_hour': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }