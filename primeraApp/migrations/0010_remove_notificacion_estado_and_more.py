# Generated by Django 5.1 on 2024-11-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0009_notificacion_estado_notificacion_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='estado',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='fecha_programada',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora programada'),
        ),
    ]
