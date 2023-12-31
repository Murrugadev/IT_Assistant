# Generated by Django 4.2.5 on 2023-09-07 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipo', models.CharField(max_length=40, null=True)),
                ('Usuario', models.CharField(max_length=40, null=True)),
                ('Estado_usuario', models.CharField(max_length=40, null=True)),
                ('PID', models.IntegerField(null=True)),
                ('Uso_CPU', models.TextField(max_length=60)),
                ('Nucleos_fisicos', models.IntegerField(null=True)),
                ('Nucleos_logicos', models.IntegerField(null=True)),
                ('Frecuencia_actual', models.TextField(null=True)),
                ('Frecuencia_minima', models.TextField(null=True)),
                ('Frecuencia_maxima', models.TextField(null=True)),
                ('Capacidad_RAM', models.FloatField(null=True)),
                ('Porcentaje_RAM', models.FloatField()),
                ('Uso_RAM', models.FloatField(null=True)),
                ('Disponibilidad_RAM', models.FloatField(null=True)),
                ('Capacidad_disco', models.FloatField(null=True)),
                ('Porcentaje_disco', models.FloatField()),
                ('Uso_disco', models.FloatField(null=True)),
                ('Disponibilidad_disco', models.FloatField(null=True)),
                ('Temperatura_actual', models.FloatField(null=True)),
                ('Temperatura_alta', models.FloatField(null=True)),
                ('Temperatura_critica', models.FloatField(null=True)),
                ('IP', models.FloatField(null=True)),
            ],
        ),
    ]
