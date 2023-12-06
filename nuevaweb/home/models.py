from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    publicacion = models.DateField()
    cantidad_disponible = models.PositiveIntegerField(default=0)

class CategoriaPieza(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class PiezaCarro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_en_stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(CategoriaPieza, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre