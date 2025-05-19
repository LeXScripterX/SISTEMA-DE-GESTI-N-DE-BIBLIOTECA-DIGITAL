from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class TipoUsuario(models.TextChoices):
    ESTUDIANTE = 'EST', _('Estudiante')
    PROFESOR = 'PRO', _('Profesor')
    BIBLIOTECARIO = 'BIB', _('Bibliotecario')
    ADMINISTRADOR = 'ADM', _('Administrador')

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ProgramaAcademico(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    tipo = models.CharField(
        max_length=3,
        choices=TipoUsuario.choices,
        default=TipoUsuario.ESTUDIANTE,
    )
    telefono = PhoneNumberField(blank=True, null=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    facultad = models.ForeignKey(
        Facultad, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    programa_academico = models.ForeignKey(
        ProgramaAcademico, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    documento_identidad = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True, 
        null=True
    )
    foto_perfil = models.ImageField(
        upload_to='perfiles/', 
        blank=True, 
        null=True
    )

    REQUIRED_FIELDS = ['email', 'tipo', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-fecha_registro']
        permissions = [
            ("puede_ver_dashboard", "Puede ver el dashboard administrativo"),
        ]

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_tipo_display()})"

    @property
    def es_administrador(self):
        return self.tipo == TipoUsuario.ADMINISTRADOR or self.is_superuser

    @property
    def es_bibliotecario(self):
        return self.tipo == TipoUsuario.BIBLIOTECARIO

    @property
    def es_profesor(self):
        return self.tipo == TipoUsuario.PROFESOR

    @property
    def es_estudiante(self):
        return self.tipo == TipoUsuario.ESTUDIANTE