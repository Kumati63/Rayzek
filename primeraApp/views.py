from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Usuario, Dispositivo, Casa, Medidor
from django.contrib.auth.hashers import check_password
from .decorators import login_required_custom # metodo que verifica el estado de la sesión
from django.contrib.auth import logout
import random, string

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
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')

    # Obtener dispositivos del usuario
    dispositivos = Dispositivo.objects.filter(casa=usuario.casa)
    
    # Obtener medidores asociados a la casa del usuario
    medidores = Medidor.objects.filter(casa=usuario.casa)

    if request.method == 'POST':
        if 'agregar' in request.POST:
            nombre = request.POST.get('nombre')
            ubicacion = request.POST.get('ubicacion')
            tipo = request.POST.get('tipo')
            medidor_id = request.POST.get('medidor')  # Obtener el ID del medidor seleccionado
            
            casa = usuario.casa
            
            try:
                # Obtener el medidor seleccionado
                medidor = Medidor.objects.get(id=medidor_id) if medidor_id else None
                
                # Crear y guardar el nuevo dispositivo
                dispositivo = Dispositivo(
                    nombre=nombre,
                    ubicacion=ubicacion,
                    tipo=tipo,
                    medidor=medidor,
                    casa=casa
                )
                dispositivo.save()
                messages.success(request, 'Dispositivo agregado exitosamente.')
            except Medidor.DoesNotExist:
                messages.error(request, 'El medidor seleccionado no existe.')
            except Exception as e:
                messages.error(request, f'Error al crear el dispositivo: {str(e)}')

        elif 'eliminar' in request.POST:
            dispositivo_id = request.POST.get('dispositivo_id')
            dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
            dispositivo.delete()
            messages.success(request, 'Dispositivo eliminado exitosamente.')

    context = {
        'usuario': usuario,
        'dispositivos': dispositivos,
        'medidores': medidores,  # Agregar medidores al contexto
    }
    
    return render(request, 'PrimeraApp/CrudDispositivos.html', context)

@login_required_custom
def CrudInvitaciones(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    return render(request,'PrimeraApp/CrudInvitaciones.html', {'usuario': usuario})

@login_required_custom
def CrudMiembros(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    return render(request,'PrimeraApp/CrudMiembros.html', {'usuario': usuario})

@login_required_custom
def wattsGraphs(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    return render(request,'PrimeraApp/wattsGraphs.html', {'usuario': usuario})

@login_required_custom
def CrudNotificaciones(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    return render(request,'PrimeraApp/CrudNotificaciones.html', {'usuario': usuario})

@login_required_custom
def Menu(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    
    return render(request,'PrimeraApp/Menu.html', {'usuario': usuario})

def logout_view(request):
    # Cerrar la sesión del usuario
    logout(request)  # Esto elimina la información de la sesión del usuario
    return redirect('Login')  # Redirigir a la página de inicio de sesión

def generate_group_code(length=10):
    """Genera un código de grupo aleatorio con caracteres especiales."""
    letters = string.ascii_uppercase + string.digits + "!@#$%&*?"
    return ''.join(random.choice(letters) for _ in range(length))

@login_required_custom
def CrudADMSignup(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('Login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        
        # Verificar si el rol del usuario es 'adm'
        if usuario.roles != 'adm':
            return redirect('Menu')
        
        # Obtener todos los usuarios
        tablaUsuarios = Usuario.objects.all()
        
        if request.method == 'POST':
            usuario_id = request.POST.get('usuario_id')
            if usuario_id:
                usuario = get_object_or_404(Usuario, id=usuario_id)
                usuario.nombre = request.POST.get('nombre')
                usuario.email = request.POST.get('email')
                
                # Actualiza la casa si es necesario
                nombre_casa = request.POST.get('Casa')
                casa, created = Casa.objects.get_or_create(nombre=nombre_casa, codigo=generate_group_code())
                usuario.casa = casa
                
                # Si se proporciona una nueva imagen de perfil
                if request.FILES.get('File'):
                    usuario.imgPerfil = request.FILES['File']
                
                usuario.save()
            else:
                # Obtener datos del formulario
                nombre = request.POST.get('nombre')
                email = request.POST.get('email')
                contraseña = request.POST.get('contrasena')
                imagen_perfil = request.FILES.get('File')
                identificador_medidor = request.POST.get('Medidor')
                nombreCasa = request.POST.get('Casa')

                # Generar código de grupo
                codigo_grupo = generate_group_code()
                # crear casa
                casa = Casa.objects.create(nombre=nombreCasa, codigo=codigo_grupo)

                # Crear usuario
                usuario = Usuario(
                    nombre=nombre, 
                    email=email, 
                    contraseña=make_password(contraseña), 
                    imgPerfil=imagen_perfil,
                    casa=casa)
                usuario.save()

                # Crear el medidor
                medidor = Medidor(identificador=identificador_medidor, casa=casa)
                medidor.save()

            return redirect('CrudADMSignup')  # Redirige a la URL de éxito
        
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')
    return render(request,'PrimeraApp/CrudADMSignup.html', {'usuario': usuario, 'tablaUsuarios': tablaUsuarios})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    # Eliminar el usuario
    usuario.delete()

    # Redirigir de vuelta a la lista de usuarios
    return redirect('CrudADMSignup')

def cambiar_estado(request, usuario_id):
    # Obtener el usuario autenticado desde la sesión
    usuario_actual_id = request.session.get('usuario_id')
    
    # Verificar si el usuario está autenticado
    if not usuario_actual_id:
        return redirect('Login')
    
    # Obtener el usuario que está logueado
    try:
        usuario_actual = Usuario.objects.get(id=usuario_actual_id)
    except Usuario.DoesNotExist:
        del request.session['usuario_id']
        return redirect('Login')

    # Obtener el usuario que se quiere modificar
    usuario = get_object_or_404(Usuario, id=usuario_id)

    # Verificar si es el usuario actual
    if usuario.id == usuario_actual.id:
        messages.error(request, "No puedes desactivar tu propio usuario.")
        return redirect('CrudADMSignup')
    
    # Cambiar estado del usuario
    nuevo_estado = 1 if usuario.estado == 0 else 0
    Usuario.objects.filter(id=usuario_id).update(estado=nuevo_estado)
    
    messages.success(request, f"El estado del usuario {usuario.nombre} ha sido actualizado.")
    return redirect('CrudADMSignup')

def obtener_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    data = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'email': usuario.email,
        'medidor_identificador': usuario.casa.medidor.identificador if usuario.casa and usuario.casa.medidor else '',
        'casa_nombre': usuario.casa.nombre if usuario.casa else '',
        'imgPerfil': usuario.imgPerfil.url if usuario.imgPerfil else None,
    }
    return JsonResponse(data)

