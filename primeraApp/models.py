from django.db import models
from datetime import datetime

# Create your models here.
usuarios = {
    1: {
        "id": 1,
        "nombre": "Marcelo",
        "email": "marcelo@a.com",
        "contraseña": "qwerty",
        "tipo": "administrador"
    },
    2: {
        "id": 2,
        "nombre": "Jeff",
        "email": "jeff@a.com",
        "contraseña": "qwerty",
        "tipo": "usuario"
    },
    3: {
        "id": 3,
        "nombre": "Matias",
        "email": "matias@a.com",
        "contraseña": "qwerty",
        "tipo": "tecnico"
    }
}

# 1 equivale a encendido y 2 a apagado

dispositivos = {
    1: {
        "id": 1,
        "nombre": "Luz Sala",
        "estado": 1,
        "tipo": "luz",
        "UmbralConsumo": 0
    },
    2: {
        "id": 2,
        "nombre": "Luz Cocina",
        "estado": 2,
        "tipo": "luz",
        "UmbralConsumo": 0
    },
    3: {
        "id": 3,
        "nombre": "Televisor",
        "estado": 1,
        "tipo": "tv",
        "UmbralConsumo": 0
    }
}

alertas = {
    1: {
        "id": 1,
        "alerta": "Consumo alto",
        "timestamp": datetime.now(),
        "usuario": "Marcelo"
    },
    2: {
        "id": 2,
        "alerta": "Dispositivo apagado",
        "timestamp": datetime.now(),
        "usuario": "Jeff"
    },
    3: {
        "id": 3,
        "alerta": "Consumo bajo",
        "timestamp": datetime.now(),
        "usuario": "Matias"
    }
}

mediciones = {
    1: {
        "id": 1,
        "dispositivo": "Luz Sala",
        "timestamp": datetime.now(),
        "consumo": 15.5
    },
    2: {
        "id": 2,
        "dispositivo": "Luz Cocina",
        "timestamp": datetime.now(),
        "consumo": 10.2
    },
    3: {
        "id": 3,
        "dispositivo": "Televisor",
        "timestamp": datetime.now(),
        "consumo": 25.3
    }
}