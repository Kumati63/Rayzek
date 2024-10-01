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
]
