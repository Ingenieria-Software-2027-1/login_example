from django.contrib import admin
from .models import Space

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price_per_hour', 'host', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)