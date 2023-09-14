from django.contrib import admin
from .models import Equipos
# Register your models here.

class EquiposAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'Equipo',
        'Usuario',
        'Estado_usuario',
        'PID',
        'Uso_CPU',
        'Nucleos_fisicos',
        'Nucleos_logicos',
        'Frecuencia_actual',
        'Frecuencia_minima',
        'Frecuencia_maxima',
        'Capacidad_RAM',
        'Porcentaje_RAM',
        'Uso_RAM',
        'Disponibilidad_RAM',
        'Capacidad_disco',
        'Porcentaje_disco',
        'Uso_disco',
        'Disponibilidad_disco',
        'Temperatura_actual',
        'Temperatura_alta',
        'Temperatura_critica',
        'IP',
        'Mascara_red'
    )

admin.site.register(Equipos,EquiposAdmin)