from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Categoria', max_length=20, blank=False, null=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nombre
    
class TipoUnidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Tipo de Unidad', max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de Unidad'
        verbose_name_plural = 'Tipos de Unidad'
        ordering = ['pk']
    
    def __str__(self):
        return self.nombre

class UnidadMedidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
    gramage = models.IntegerField('Gramage', blank=False, null=False)
    tipoUnidad = models.ForeignKey(TipoUnidad, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'
        ordering = ['pk']

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=40, blank=40, null=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)
    tipoUnidad = models.ForeignKey(TipoUnidad, on_delete=models.CASCADE, blank=False, null=False)
    manejaInventario = models.BooleanField('Maneja Inventario', default=False)
    redondeo = models.BooleanField('Redondear a unidades', default=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nombre
