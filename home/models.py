from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    def __str__ (self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre       = models.CharField(max_length = 100)
    descripcion  = models.CharField(max_length = 500)
    status       = models.BooleanField( default = True)
    precio       = models.DecimalField(max_digits = 9, decimal_places=2)
    stok         = models.IntegerField()
    Categorias   = models.ManyToManyField(Categoria, null= True, blank= True)
    marca        = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + str(self.precio)