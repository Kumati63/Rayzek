# Generated by Django 5.1 on 2024-11-12 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0008_alter_dispositivo_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Estado de la notificación (Leída/No leída)'),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notificaciones', to='primeraApp.usuario'),
        ),
    ]