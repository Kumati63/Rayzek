# Generated by Django 4.2.7 on 2024-10-21 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0004_casa_dispositivo_alter_usuario_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casa',
            options={'managed': True, 'verbose_name': 'casa', 'verbose_name_plural': 'casas'},
        ),
        migrations.AlterModelOptions(
            name='dispositivo',
            options={'managed': True, 'verbose_name': 'dispositivo', 'verbose_name_plural': 'dispositivos'},
        ),
        migrations.AlterModelOptions(
            name='historial',
            options={'managed': True, 'verbose_name': 'historial', 'verbose_name_plural': 'historiales'},
        ),
        migrations.AlterModelOptions(
            name='medicion',
            options={'managed': True, 'verbose_name': 'medición', 'verbose_name_plural': 'mediciones'},
        ),
        migrations.AlterModelOptions(
            name='medidor',
            options={'managed': True, 'verbose_name': 'medidor', 'verbose_name_plural': 'medidores'},
        ),
        migrations.AlterModelOptions(
            name='notificacion',
            options={'managed': True, 'verbose_name': 'notificación', 'verbose_name_plural': 'notificaciones'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': True, 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AlterModelTable(
            name='casa',
            table='casa',
        ),
        migrations.AlterModelTable(
            name='dispositivo',
            table='dispositivo',
        ),
        migrations.AlterModelTable(
            name='historial',
            table='historial',
        ),
        migrations.AlterModelTable(
            name='medicion',
            table='medicion',
        ),
        migrations.AlterModelTable(
            name='medidor',
            table='medidor',
        ),
        migrations.AlterModelTable(
            name='notificacion',
            table='notificacion',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]
