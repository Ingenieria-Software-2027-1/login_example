from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    is_renter = models.BooleanField(default=False, verbose_name= "Es arrendatario")
    is_host = models.BooleanField(default=False, verbose_name="Es anfitrion")
    phone_numer = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefono")
    
    def __str__(self):
        
        rol = "Anfitrion" if self.is_host else "Arrendatario"
        return f"{self.username} - {rol}"