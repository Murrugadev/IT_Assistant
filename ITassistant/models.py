from django.db import models

# Create your models here.

class Devices(models.Model):
    Equipo= models.CharField(blank=False,null=True,max_length=40)
    Usuario = models.CharField(blank=False,null=True,max_length=40)
    Estado_usuario= models.CharField(blank=False,null=True,max_length=40)
    PID= models.IntegerField(blank=False,null=True)
    Uso_CPU= models.TextField(blank=False,max_length=60)
    Nucleos_fisicos= models.IntegerField(blank=False,null=True)
    Nucleos_logicos= models.IntegerField(blank=False,null=True)
    Frecuencia_actual= models.CharField(blank=False,null=True, max_length=10)
    Frecuencia_minima= models.CharField(blank=False,null=True,max_length=10)
    Frecuencia_maxima= models.CharField(blank=False,null=True,max_length=10)
    Capacidad_RAM= models.CharField(blank=False,null=True,max_length=10)
    Porcentaje_RAM= models.CharField(blank=False,null=True,max_length=10)
    Uso_RAM= models.CharField(blank=False,null=True,max_length=10)
    Disponibilidad_RAM= models.CharField(blank=False,null=True,max_length=10)
    Capacidad_disco= models.CharField(blank=False,null=True,max_length=10)
    Porcentaje_disco= models.CharField(blank=False,null=True,max_length=10)
    Uso_disco= models.CharField(blank=False,null=True,max_length=10)
    Disponibilidad_disco= models.CharField(blank=False,null=True,max_length=10)
    Temperatura_actual= models.CharField(blank=False, null=True,max_length=10)
    Temperatura_alta= models.CharField(blank=False,null=True,max_length=10)
    Temperatura_critica= models.CharField(blank=False, null=True,max_length=10)
    IP= models.TextField(blank=False, null=True)
    Mascara_red = models.TextField(blank=False, null=True)