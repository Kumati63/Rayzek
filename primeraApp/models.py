
from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from primeraApp.choises import roles

class Casa(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del grupo")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código del grupo")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'casa'
        managed = True
        verbose_name = 'casa'
        verbose_name_plural = 'casas'

class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del usuario")
    email = models.EmailField(max_length=255, unique=True)
    contraseña = models.CharField(max_length=255)
    imgPerfil = models.ImageField(upload_to='imgPerfil/', null=True, blank=True)
    roles = models.CharField(max_length=3, validators=[MinLengthValidator(3)], default='usu', verbose_name="roles del usuario")
    estado = models.IntegerField(default=1)
    casa = models.ForeignKey(Casa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Grupo Familiar")
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"
    
    class Meta:
        db_table = 'usuario'
        managed = True
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class Medidor(models.Model):
    identificador = models.CharField(max_length=50, unique=True, verbose_name="Identificador del medidor")
    casa = models.OneToOneField(Casa, on_delete=models.CASCADE, related_name="medidor", verbose_name="Grupo familiar vinculado")

    def __str__(self):
        return f"Medidor {self.identificador} - Casa: {self.casa.nombre}"
    
    class Meta:
        db_table = 'medidor'
        managed = True
        verbose_name = 'medidor'
        verbose_name_plural = 'medidores'

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del dispositivo")
    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE, verbose_name="Medidor vinculado", related_name="dispositivos")
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, verbose_name="Grupo familiar", related_name="dispositivos")
    ubicacion = models.CharField(max_length=100, verbose_name="ubicación del dispositivo", null=True, blank=True)
    tipo = models.CharField(max_length=100, verbose_name="Tipo de dispositivo", null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'dispositivo'
        managed = True
        verbose_name = 'dispositivo'
        verbose_name_plural = 'dispositivos'

class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="mediciones")
    fecha = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField(verbose_name="Consumo en kWh")

    def __str__(self):
        return f"Medición {self.id} - {self.dispositivo.nombre}"
    
    class Meta:
        db_table = 'medicion'
        managed = True
        verbose_name = 'medición'
        verbose_name_plural = 'mediciones'

class Historial(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="historial")
    fecha = models.DateField()
    consumo_total = models.FloatField(verbose_name="Consumo total diario en kWh")

    def __str__(self):
        return f"Historial {self.id} - {self.dispositivo.nombre}"
    
    class Meta:
        db_table = 'historial'
        managed = True
        verbose_name = 'historial'
        verbose_name_plural = 'historiales'

class Notificacion(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name="notificaciones")
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="notificaciones")
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.SET_NULL, null=True, blank=True, related_name="notificaciones")
    mensaje = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField(null=True, blank=True, verbose_name="Fecha y hora programada")

    def __str__(self):
        return f"Notificación para {self.casa.nombre} - {self.fecha_programada}"
    
    class Meta:
        db_table = 'notificacion'
        managed = True
        verbose_name = 'notificación'
        verbose_name_plural = 'notificaciones'