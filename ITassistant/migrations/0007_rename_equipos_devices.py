# Generated by Django 4.2.5 on 2023-09-25 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITassistant', '0006_alter_equipos_capacidad_ram_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipos',
            new_name='Devices',
        ),
    ]