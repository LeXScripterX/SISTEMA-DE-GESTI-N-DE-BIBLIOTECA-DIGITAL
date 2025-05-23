# Generated by Django 5.1 on 2025-04-22 03:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo', '0002_initial'),
        ('ejemplares', '0002_initial'),
        ('prestamos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='aprobado_por',
            field=models.ForeignKey(blank=True, limit_choices_to={'tipo__in': ['BIB', 'ADM']}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prestamos_aprobados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='ejemplar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ejemplares.ejemplar'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='multa',
            name='prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.recursodigital'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
