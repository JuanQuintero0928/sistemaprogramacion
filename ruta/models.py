from django.db import models

# Create your models here.

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Departamento', max_length=20, null=False, blank=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Municipio', max_length=30, null=False, blank=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nombre
    
class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Ruta', max_length=40, null=False, blank=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nombre

class CentroAcopio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Centro de Acopio', max_length=40, null=False, blank=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Centro de Acopio'
        verbose_name_plural = 'Centros de Acopio'
        ordering = ['pk']

    def __str__(self):
        return self.nombre