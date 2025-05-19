from django.db import models
from django.utils.translation import gettext_lazy as _

class EstadoPrestamo(models.TextChoices):
    SOLICITADO = 'SOL', _('Solicitado')
    APROBADO = 'APR', _('Aprobado')
    RECHAZADO = 'REC', _('Rechazado')
    EN_CURSO = 'CUR', _('En curso')
    DEVUELTO = 'DEV', _('Devuelto')
    VENCIDO = 'VEN', _('Vencido')
    CANCELADO = 'CAN', _('Cancelado')

class Prestamo(models.Model):
    ejemplar = models.ForeignKey('ejemplares.Ejemplar', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(
        max_length=3,
        choices=EstadoPrestamo.choices,
        default=EstadoPrestamo.SOLICITADO,
    )
    aprobado_por = models.ForeignKey(
        'usuarios.Usuario', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='prestamos_aprobados',
        limit_choices_to={'tipo__in': ['BIB', 'ADM']}
    )
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.ejemplar} - {self.usuario}"

class Reserva(models.Model):
    recurso = models.ForeignKey('catalogo.RecursoDigital', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_reserva = models.DateTimeField()
    estado = models.CharField(
        max_length=3,
        choices=EstadoPrestamo.choices,
        default=EstadoPrestamo.SOLICITADO,
    )
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.recurso} - {self.usuario}"

class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    pagada = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Multa'
        verbose_name_plural = 'Multas'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Multa #{self.id} - {self.prestamo}"