
from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from primeraApp.choises import roles

class Usuario(models.Model):
    nombre = models.CharField(max_length=255,verbose_name="Nombre del usuario")
    email = models.EmailField(max_length=255, unique=True)
    contraseña = models.CharField(max_length=255)
    imgPerfil = models.ImageField(upload_to='imgPerfil/', null=True, blank=True)
    roles = models.CharField(max_length=3, validators=[MinLengthValidator(3)],choices=roles,default='usu',verbose_name="roles del usuario")
    estado = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'usuario'
        managed = True
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
