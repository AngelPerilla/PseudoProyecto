# Generated by Django 5.1 on 2024-08-30 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0005_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Documento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_genero',
            field=models.CharField(blank=True, choices=[('', 'Seleccione una opción'), ('FEM', 'Femenino'), ('MASC', 'Masculino'), ('OTRO', 'Otro')], max_length=4),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellidos',
            field=models.CharField(max_length=80, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='documento',
            field=models.CharField(max_length=20, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombres',
            field=models.CharField(max_length=80, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_documento',
            field=models.CharField(blank=True, choices=[('', 'Seleccione una opción'), ('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extrangería'), ('NIT', 'Número de Identificación Tributaria (NIT)'), ('TI', 'Tarjeta de identidad')], max_length=4),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=60, unique=True, verbose_name='Nombre'),
        ),
    ]
