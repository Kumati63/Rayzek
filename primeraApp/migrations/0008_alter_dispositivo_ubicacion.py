# Generated by Django 4.2.7 on 2024-10-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0007_dispositivo_tipo_dispositivo_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ubicación del dispositivo'),
        ),
    ]
