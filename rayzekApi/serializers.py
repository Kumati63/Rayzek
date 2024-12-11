from rest_framework import serializers
from primeraApp.models import Usuario

class UsuariosSerializar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DispositivosSerializar(serializers.ModelSerializer):
    class Meta:
        model = Dispositivos
        fields = '__all__'