from rest_framework import serializers
from primeraApp.models import Usuario

class UsuariosSerializar(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_email(self, value):
        if Usuario.objects.exclude(id=self.instance.id).filter(email=value).exists():
            raise serializers.ValidationError("Ya existe usuario con este email.")
        return value