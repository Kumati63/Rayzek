from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from primeraApp.models import Usuario, Dispositivo
from rayzekApi.serializers import UsuariosSerializar, DispositivoSerializar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
def usuariosApi(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios':list(
            usuarios.values('nombre','email','contraseña','imgPerfil','roles','estado','casa')
        )
    }
    return JsonResponse(data)

@api_view(['GET','POST'])
def usuario_listado(request):
    if request.method == 'GET':
        Usuarios = Usuario.objects.all()
        serializer= UsuariosSerializar(Usuarios,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UsuariosSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def usuarios_detalles(request,pk):
    try:
        usuario = Usuario.objects.get(id=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = UsuariosSerializar(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UsuariosSerializar(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def dispositivosApi(request):
    dispositivos = Dispositivo.objects.all()
    data = {
        'dispositivos':list(
            dispositivos.values('nombre','casa','ubicacion','tipo')
        )
    }
    return JsonResponse(data)

@api_view(['GET','POST'])
def dispositivo_listado(request):
    if request.method == 'GET':
        dispositivos = Dispositivo.objects.all()
        serializer= DispositivoSerializar(dispositivos,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DispositivoSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Dispositivos_detalles(request,pk):
    try:
        dispositivo = Dispositivo.objects.get(id=pk)
    except Dispositivo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = DispositivoSerializar(dispositivo)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DispositivoSerializar(dispositivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        dispositivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)