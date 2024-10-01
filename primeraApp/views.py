from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def landingPage(request):
    return render(request,'PrimeraApp\LandingPage.html')

def Login(request):
    return render(request,'PrimeraApp\Login.html')

def Signup(request):
    return render(request,'PrimeraApp\Signup.html')
