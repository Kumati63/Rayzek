from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password
from .decorators import login_required_custom # metodo que verifica el estado de la sesión
from django.contrib.auth import logout


# Create your views here.
def landingPage(request):
    
    return render(request,'PrimeraApp/LandingPage.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('contrasena')

        try:
            # Verificar si el email existe
            user = Usuario.objects.get(email=email)

            # Obtener el contador de intentos fallidos
            failed_attempts = request.session.get(f'failed_attempts_{email}', 0)

            # Si la cuenta está activa y los intentos fallidos son 3, reiniciar contador
            if user.estado == 1 and failed_attempts >= 3:
                request.session[f'failed_attempts_{email}'] = 0
                failed_attempts = 0  # Reiniciar el contador si la cuenta está desbloqueada

            # Usar check_password para verificar la contraseña hasheada
            if check_password(password, user.contraseña):  # Validar la contraseña
                # Verificar si la cuenta está activa
                if user.estado == 1:
                    # Reiniciar el contador de intentos fallidos al iniciar sesión correctamente
                    request.session[f'failed_attempts_{email}'] = 0
                    # Iniciar sesión manualmente guardando el usuario en la sesión
                    request.session['usuario_id'] = user.id
                    return redirect('Menu')

            else:
                # Incrementar el contador de intentos fallidos si la contraseña es incorrecta
                failed_attempts += 1
                request.session[f'failed_attempts_{email}'] = failed_attempts

                if failed_attempts == 3:
                    # Bloquear la cuenta usando update()
                    Usuario.objects.filter(email=email).update(estado=0)
                    messages.error(request, 'Cuenta bloqueada por múltiples intentos fallidos')
                else:
                    remaining_attempts = 3 - failed_attempts
                    messages.error(request, f'Contraseña incorrecta. Intentos restantes: {remaining_attempts}')

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
        rol = 'usu'  # se establece el rol de usuario por defecto

        # Crear el usuario
        usuario = Usuario(
            nombre=nombre,
            email=email,
            contraseña=make_password(contrasena),  # Encriptar la contraseña
            imgPerfil=imgPerfil,
            estado=1,  # Puedes asignar un valor por defecto al estado
            roles=rol,
            casa=None  # No asignar ninguna casa inicialmente
        )
        usuario.save()

        messages.success(request, "Usuario registrado exitosamente")
        return redirect('Login')

    return render(request, 'PrimeraApp/Signup.html')

@login_required_custom
def main(request):
    
    return render(request,'PrimeraApp/main.html')

@login_required_custom
def CrudDispositivos(request):
    
    return render(request,'PrimeraApp/CrudDispositivos.html')

@login_required_custom
def CrudInvitaciones(request):
    return render(request,'PrimeraApp/CrudInvitaciones.html')

@login_required_custom
def CrudMiembros(request):
    return render(request,'PrimeraApp/CrudMiembros.html')

@login_required_custom
def wattsGraphs(request):
    return render(request,'PrimeraApp/wattsGraphs.html')

@login_required_custom
def CrudNotificaciones(request):
    return render(request,'PrimeraApp/CrudNotificaciones.html')

@login_required_custom
def Menu(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        print(f"Usuario recuperado: {usuario}")
        print(f"Nombre del usuario: {usuario.nombre}")
        print(f"Email del usuario: {usuario.email}")
        print(f"Rol del usuario: {usuario.roles}")
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    
    return render(request,'PrimeraApp/Menu.html', {'usuario': usuario})

def logout_view(request):
    # Cerrar la sesión del usuario
    logout(request)  # Esto elimina la información de la sesión del usuario
    return redirect('Login')  # Redirigir a la página de inicio de sesión