from django.contrib import admin
from django.urls import path
from primeraApp import views

urlpatterns = [
    path('', views.landingPage,name='landingPage'),
    path('Login/', views.Login,name='Login'),
    path('Signup/', views.Signup,name='Signup'),
    path('main/', views.main,name='main'),
    path('CrudNotificaciones/', views.CrudNotificaciones,name='CrudNotificaciones'),
    path('CrudDispositivos/', views.CrudDispositivos,name='CrudDispositivos'),
    path('CrudInvitaciones/', views.CrudInvitaciones,name='CrudInvitaciones'),
    path('Menu/', views.Menu,name='Menu'),
    path('wattsGraphs/', views.wattsGraphs,name='wattsGraphs'),
    path('CrudMiembros/', views.CrudMiembros,name='CrudMiembros'),
]
