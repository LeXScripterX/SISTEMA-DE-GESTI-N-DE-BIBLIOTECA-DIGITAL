# Generated by Django 5.1 on 2025-04-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('datos', models.JSONField(default=dict)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Estadística',
                'verbose_name_plural': 'Estadísticas',
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('PRE', 'Préstamos'), ('REC', 'Recursos'), ('USU', 'Usuarios'), ('MUL', 'Multas'), ('INV', 'Inventario')], max_length=3)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('parametros', models.JSONField(default=dict)),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='reportes/')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'ordering': ['-fecha_generacion'],
            },
        ),
    ]
