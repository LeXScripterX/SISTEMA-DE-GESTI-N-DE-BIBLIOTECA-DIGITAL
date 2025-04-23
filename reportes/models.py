from django.db import models
from django.utils.translation import gettext_lazy as _

class TipoReporte(models.TextChoices):
    PRESTAMOS = 'PRE', _('Préstamos')
    RECURSOS = 'REC', _('Recursos')
    USUARIOS = 'USU', _('Usuarios')
    MULTAS = 'MUL', _('Multas')
    INVENTARIO = 'INV', _('Inventario')

class Reporte(models.Model):
    tipo = models.CharField(max_length=3, choices=TipoReporte.choices)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    parametros = models.JSONField(default=dict)
    generado_por = models.ForeignKey(
        'usuarios.Usuario', 
        on_delete=models.SET_NULL, 
        null=True,
        limit_choices_to={'tipo__in': ['BIB', 'ADM']}
    )
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    archivo = models.FileField(upload_to='reportes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['-fecha_generacion']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nombre}"

class Estadistica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    datos = models.JSONField(default=dict)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Estadística'
        verbose_name_plural = 'Estadísticas'

    def __str__(self):
        return self.nombre