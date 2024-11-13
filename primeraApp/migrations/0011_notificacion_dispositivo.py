# Generated by Django 5.1 on 2024-11-12 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0010_remove_notificacion_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='dispositivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notificaciones', to='primeraApp.dispositivo'),
        ),
    ]
