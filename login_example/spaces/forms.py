from django import forms
from .models import Space

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'description', 'capacity', 'price_per_hour', 'is_available']