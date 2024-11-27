from django.contrib import admin
from django.urls import path, include
from primeraApp import views
from .views import MedicionDataView


urlpatterns = [
    path('', views.landingPage,name='landingPage'),
    path('Login/', views.Login,name='Login'),
    path('Signup/', views.Signup,name='Signup'),
    path('main/', views.main,name='main'),
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
]
