from django.contrib import admin
from .models import Space

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'capacity', 'price_per_hour', 'is_available', 'created_at')
    list_filter = ('is_available',)
    search_fields = ('name', 'host__username')
# Register your models here.
