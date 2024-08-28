from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField(null=True)
    cantidad = models.IntegerField(null=True)