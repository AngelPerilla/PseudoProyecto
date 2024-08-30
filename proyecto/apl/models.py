from django.db import models
from datetime import datetime
class Producto (models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre', unique=True)
    precio = models.IntegerField(null=True)
    cantidad = models.IntegerField(null=True)
    def __str__(self):
        return self.nombre

    class meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = [id]

class Persona (models.Model):
    nombres = models.CharField(max_length=80, verbose_name='Nombres')
    apellidos = models.CharField(max_length=80, verbose_name='Apellidos')
    documento = models.CharField(max_length=20, verbose_name='Documento')
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=20, verbose_name='Nombre')
    direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Documento')
    femenino = 'FEM'
    masculino = 'MASC'
    otro = 'OTRO'
    opciones_genero = {
        femenino: 'Femenino',
        masculino: 'Masculino',
        otro: 'Otro'
    }
    tipo_genero = models.CharField(
        max_length=4,
        choices=[('','Seleccione una opción')] + list(opciones_genero.items()),
        blank=True
    )
    cedula_c = 'CC'
    cedula_e = 'CE'
    nit = 'NIT'
    tarjeta_i = 'TI'
    opciones_documento = {
        cedula_c: 'Cédula de ciudadanía',
        cedula_e: 'Cédula de extrangería',
        nit: 'Número de Identificación Tributaria (NIT)',
        tarjeta_i: 'Tarjeta de identidad'
    }
    tipo_documento = models.CharField(
        max_length=4,
        choices=[('','Seleccione una opción')] + list(opciones_documento.items()),
        blank=True
    )
    def __str__(self):
        return self.nombres
    
    class meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Persona'
        db_table = 'Persona'
        ordering = [id]
    