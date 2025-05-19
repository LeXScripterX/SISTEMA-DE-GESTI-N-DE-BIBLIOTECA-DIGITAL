from django.db import models
from django.utils.translation import gettext_lazy as _

class EstadoEjemplar(models.TextChoices):
    DISPONIBLE = 'DIS', _('Disponible')
    PRESTADO = 'PRE', _('Prestado')
    RESERVADO = 'RES', _('Reservado')
    EN_REPARACION = 'REP', _('En reparación')
    PERDIDO = 'PER', _('Perdido')
    RETIRADO = 'RET', _('Retirado')

class Ejemplar(models.Model):
    recurso = models.ForeignKey('catalogo.RecursoDigital', on_delete=models.CASCADE)
    codigo_barras = models.CharField(max_length=50, unique=True)
    estado = models.CharField(
        max_length=3,
        choices=EstadoEjemplar.choices,
        default=EstadoEjemplar.DISPONIBLE,
    )
    ubicacion = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notas = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ejemplar'
        verbose_name_plural = 'Ejemplares'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.recurso.titulo} - {self.codigo_barras}"

class HistorialEstado(models.Model):
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE, related_name='historial_estados')
    estado_anterior = models.CharField(max_length=3, choices=EstadoEjemplar.choices)
    estado_nuevo = models.CharField(max_length=3, choices=EstadoEjemplar.choices)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(
        'usuarios.Usuario', 
        on_delete=models.SET_NULL, 
        null=True,
        limit_choices_to={'tipo__in': ['BIB', 'ADM']}
    )
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Historial de Estado'
        verbose_name_plural = 'Historial de Estados'
        ordering = ['-fecha_cambio']

    def __str__(self):
        return f"{self.ejemplar} - {self.get_estado_nuevo_display()}"