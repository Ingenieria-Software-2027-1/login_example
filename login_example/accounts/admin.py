from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    
    list_display = ('username', 'email', 'is_renter', 'is_host', 'is_staff') # Las columnas que nos interesan ver 
    
    list_filter = ('is_host', 'is_renter', 'is_staff', 'is_superuser') # Atributos para filtrar
    
    fieldsets = UserAdmin.fieldsets + (
        (
            'Roles de administracion', # Titulo de la seccion
            {
                'fields': (
                    'is_renter',
                    'is_host',
                    'phone_numer'
                )
            }
        ),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)    