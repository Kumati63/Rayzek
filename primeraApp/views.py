from django.shortcuts import render
from django.http import HttpResponse
from primeraApp.models import alertas
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def landingPage(request):
    return render(request,'PrimeraApp\LandingPage.html')

def Login(request):
    return render(request,'PrimeraApp\Login.html')

def Signup(request):
    return render(request,'PrimeraApp\Signup.html')

def main(request):
    return render(request,'PrimeraApp\main.html')

def CrudDispositivos(request):
    return render(request,'PrimeraApp\CrudDispositivos.html')


"""
Este es un método temporal para guardar cosas en la página. El modelo no se actualiza con los datos y al reiniciar la página se eliminan.
Para cambiar eso, debemos trabajar o con una base de datos o un JSON.
"""
def CrudNotificaciones(request):
    # Comprueba si llegan datos del formulario
    if request.method == 'POST':
        # Obteniene los datos del formulario
        alerta = request.POST.get('alerta')
        timestamp = request.POST.get('timestamp')
        usuario = request.POST.get('usuario')

        # Crear una nueva alerta 
        new_id = max(alertas.keys()) + 1  # Asigna el siguiente ID disponible
        alertas[new_id] = {
            "id": new_id,
            "alerta": alerta,
            "timestamp": datetime.strptime(timestamp, '%Y-%m-%dT%H:%M'),
            "usuario": usuario
        }

        # Redirigir a la página de notificaciones para evitar el reenvío del formulario al refrescar
        return redirect('CrudNotificaciones')
    #Envia datos del modelo 
    data = {
        'alertas': alertas
    }
    return render(request,'PrimeraApp\CrudNotificaciones.html',data)

