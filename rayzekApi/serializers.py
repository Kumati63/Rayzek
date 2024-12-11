from rest_framework import serializers
from primeraApp.models import Usuario

class UsuariosSerializar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DispositivoSerializar(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'