from django.db import models
from django.conf import settings

class Space(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    capacity = models.PositiveIntegerField(verbose_name="Capacidad (personas)")
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio por hora")
    is_available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="spaces",
        verbose_name="Anfitrión"
    )

    def __str__(self):
        return f"{self.name} ({self.host.username})"

# Create your models here.
