from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from primeraApp.models import Usuario
from django.contrib.auth.hashers import check_password

# Create your views here.
def landingPage(request):
    
    return render(request,'PrimeraApp\LandingPage.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('contrasena')

        try:
            # Verificar si el email existe
            user = Usuario.objects.get(email=email)

            # Usar check_password para verificar la contraseña hasheada
            if check_password(password, user.contraseña):  # Validar la contraseña
            
                if user.estado == 1:
                    # Iniciar sesión manualmente guardando el usuario en la sesión
                    request.session['usuario_id'] = user.id
                    return redirect('Menu')
            else:
                messages.error(request, 'Contraseña incorrecta')
        except Usuario.DoesNotExist:
            messages.error(request, 'Email no registrado')
    
    return render(request, 'PrimeraApp/Login.html')

def Signup(request):
    
    # Toma los datos ingresados en el formulario del signup
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        contrasena2 = request.POST['contrasena2']
        imgPerfil = request.FILES.get('File', None)
        rol = request.POST.get('roles')  # Obtén el rol del formulario

        # Crear el usuario
        usuario = Usuario(
            nombre=nombre,
            email=email,
            contraseña=make_password(contrasena),  # Encriptar la contraseña
            imgPerfil=imgPerfil,
            estado=1,  # Puedes asignar un valor por defecto al estado
            roles=rol
        )
        usuario.save()

        messages.success(request, "Usuario registrado exitosamente")
        return redirect('Login')

    return render(request, 'PrimeraApp/Signup.html')

def main(request):
    return render(request,'PrimeraApp\main.html')

def CrudDispositivos(request):
    
    return render(request,'PrimeraApp\CrudDispositivos.html')

def CrudInvitaciones(request):
    return render(request,'PrimeraApp\CrudInvitaciones.html')

def wattsGraphs(request):
    return render(request,'PrimeraApp\wattsGraphs.html')

def CrudNotificaciones(request):
    return render(request,'PrimeraApp\CrudNotificaciones.html')

def Menu(request):
    return render(request,'PrimeraApp\Menu.html')

