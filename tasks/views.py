from django.shortcuts import render
from .models import DatosPersonales, ExperienciaLaboral, Curso, Reconocimiento, ProyectoGarage

def home(request):
    datos = DatosPersonales.objects.first()
    return render(request, 'home.html', {'datos': datos})

def perfil_view(request):
    datos = DatosPersonales.objects.first()
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'perfil.html', {'datos': datos, 'experiencias': experiencias})

def imprimir_cv(request):
    datos = DatosPersonales.objects.first()
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'cv_profesional.html', {'datos': datos, 'experiencias': experiencias})

def experiencia(request): 
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'experiencia.html', {'experiencias': experiencias})

def cursos(request): 
    lista_cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': lista_cursos})

def reconocimientos(request): 
    lista_reconocimientos = Reconocimiento.objects.all()
    return render(request, 'reconocimientos.html', {'reconocimientos': lista_reconocimientos})

def garage(request): 
    productos = ProyectoGarage.objects.all()
    return render(request, 'garage.html', {'proyectos': productos})

# ESTA ES LA FUNCIÓN QUE TE DABA EL ERROR:
def productos_academicos(request): 
    return render(request, 'productos_academicos.html')