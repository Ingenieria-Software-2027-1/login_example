from django.db import models
from django.conf import settings

class Space(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del Espacio")
    description = models.TextField(verbose_name="Descripción")
    capacity = models.PositiveIntegerField(verbose_name="Capacidad (Personas)")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio por Hora ($)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='spaces',
        verbose_name="Anfitrión"
    )

    class Meta:
        verbose_name = "Espacio"
        verbose_name_plural = "Espacios"
        ordering = ['-created_at']

    def __str__(self):
        return self.name