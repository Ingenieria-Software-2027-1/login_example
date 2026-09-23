from django.contrib import admin

from .models import Space


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ("nombre", "anfitrion", "capacidad", "precio_hora", "disponible")
    list_filter = ("disponible",)
    search_fields = ("nombre", "anfitrion__username")
