from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Servicio  # Asegúrate de tener el modelo importado

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def servicios(request):
    return render(request, "core/servicios.html")

