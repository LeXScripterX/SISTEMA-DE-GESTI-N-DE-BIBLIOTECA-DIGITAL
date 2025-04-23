from django.db import models
from django.utils.translation import gettext_lazy as _

class RecursoDigital(models.Model):
    class TipoRecurso(models.TextChoices):
        LIBRO = 'LIB', _('Libro')
        REVISTA = 'REV', _('Revista')
        ARTICULO = 'ART', _('Artículo')
        TESIS = 'TES', _('Tesis')
        AUDIO = 'AUD', _('Audio')
        VIDEO = 'VID', _('Video')
        SOFTWARE = 'SOF', _('Software')
        OTRO = 'OTR', _('Otro')

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    tipo = models.CharField(max_length=3, choices=TipoRecurso.choices)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    editorial = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    doi = models.CharField(max_length=50, blank=True, null=True)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    archivo_digital = models.FileField(upload_to='recursos/', blank=True, null=True)
    url_externa = models.URLField(blank=True, null=True)
    palabras_clave = models.CharField(max_length=200, blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Recurso Digital'
        verbose_name_plural = 'Recursos Digitales'
        ordering = ['-fecha_ingreso']

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    recursos = models.ManyToManyField(RecursoDigital, related_name='categorias')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    recursos = models.ManyToManyField(RecursoDigital, related_name='colecciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(
        'usuarios.Usuario', 
        on_delete=models.SET_NULL, 
        null=True,
        limit_choices_to={'tipo__in': ['BIB', 'ADM']}
    )

    class Meta:
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'

    def __str__(self):
        return self.nombre

