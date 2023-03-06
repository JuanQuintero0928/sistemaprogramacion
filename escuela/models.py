from django.db import models
from ruta.models import *

# Create your models here.

class Escuela(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=50, null=False, blank=False)
    cod_dane = models.IntegerField('Codigo Dane', null=False, blank=False, default=99)
    centroAcopio = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE, blank=False, null=False)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=False, null=False)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'
        ordering = ['pk']
    
    def __str__(self):
        return self.nombre

class Cupo(models.Model):
    id = models.AutoField(primary_key=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, blank=False, null=False)
    cupos = models.IntegerField('Cupos')

    class Meta:
        verbose_name = 'Cupos'
        verbose_name_plural = 'Cupos'

    def __str__(self):
        return self.cupos

