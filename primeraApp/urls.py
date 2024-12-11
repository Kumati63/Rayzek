from django.contrib import admin
from django.urls import path, include
from primeraApp import views
from .views import MedicionDataView, DispositivosView
from rayzekApi import views as vistaApis

urlpatterns = [
    path('', views.landingPage,name='landingPage'),
    path('Login/', views.Login,name='Login'),
    path('Signup/', views.Signup,name='Signup'),
    path('main/', views.main,name='main'),
    path('mailResultGood/', views.mailResultGood,name='mailResultGood'),
    path('mailResultBad/', views.mailResultBad,name='mailResultBad'),
    path('userSettings/', views.userSettings,name='userSettings'),
    path('CrudNotificaciones/', views.CrudNotificaciones, name='CrudNotificaciones'),
    path('notificaciones/editar/', views.CrudNotificaciones, name='editar_notificacion'),
    path('notificaciones/eliminar/', views.CrudNotificaciones, name='eliminar_notificacion'),
    path('CrudDispositivos/', views.CrudDispositivos,name='CrudDispositivos'),
    path('CrudInvitaciones/', views.CrudInvitaciones,name='CrudInvitaciones'),
    path('Menu/', views.Menu,name='Menu'),
    path('wattsGraphs/', views.wattsGraphs,name='wattsGraphs'),
    path('CrudMiembros/', views.CrudMiembros,name='CrudMiembros'),
    path('logout/', views.logout_view, name='logout'),  # URL para cerrar sesión
    path('CrudADMSignup/', views.CrudADMSignup,name='CrudADMSignup'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_dispositivo/<int:DispositivoId>/', views.eliminar_dispositivo, name='eliminar_dispositivo'),
    path('cambiar-estado/<int:usuario_id>/', views.cambiar_estado, name='cambiar_estado'),
    path('usuarios/<int:usuario_id>/', views.obtener_usuario, name='obtener_usuario'),
    path('verificar_email/', views.verificar_email, name='verificar_email'),
    path('mediciones/', MedicionDataView.as_view(), name='medicion_data'),
    path('dispositivos/', DispositivosView.as_view(), name='dispositivos_data'),
    path('confirmar-invitacion/', views.confirmar_invitacion, name='confirmar_invitacion'),
    
    # Rutas a las api restful
    path('usuariosApi/', vistaApis.usuariosApi,name='usuariosApi'),
    path('usuariosListApi/', vistaApis.usuario_listado,name='usuariosListApi'),
    path('usuariosListApi/<int:pk>', vistaApis.usuarios_detalles,name='usuariosDetalleApi'),
    path('dispositivosApi/', vistaApis.dispositivoApi,name='dispositivosApi'),
    path('dispositivosListApi/', vistaApis.dispositivo_listado,name='dispositivosListApi'),
    path('dispositivosListApi/<int:pk>', vistaApis.dispositivos_detalles,name='dispositivosDetalleApi'),
]
