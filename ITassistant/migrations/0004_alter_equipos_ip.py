# Generated by Django 4.2.5 on 2023-09-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITassistant', '0003_alter_equipos_porcentaje_ram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='IP',
            field=models.TextField(null=True),
        ),
    ]