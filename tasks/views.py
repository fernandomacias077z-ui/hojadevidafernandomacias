from django.shortcuts import render
from .models import DatosPersonales, ExperienciaLaboral

def home(request):
    datos = DatosPersonales.objects.first()
    context = {
        'nombre': datos.nombre if datos else 'Bruno Fernando Macias Moreira',
        'ubicacion': datos.origen if datos else 'Manta, Ecuador',
        'telefono': datos.telefono if datos else '0980643265',
        'email': 'Franyo678@gmail.com'
    }
    return render(request, 'home.html', context)

def perfil_view(request):
    datos = DatosPersonales.objects.first()
    # Traemos las experiencias para que el resumen aparezca en el perfil
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'perfil.html', {
        'datos': datos,
        'experiencias': experiencias
    })

# --- ESTA ES LA VISTA QUE FALTABA ---
def imprimir_cv(request):
    datos = DatosPersonales.objects.first()
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'cv_profesional.html', {
        'datos': datos,
        'experiencias': experiencias
    })

def experiencia(request): 
    # Esta vista es para la página detallada de experiencia
    experiencias = ExperienciaLaboral.objects.all().order_by('-id')
    return render(request, 'experiencia.html', {'experiencias': experiencias})

# --- Vistas para las secciones adicionales ---
def cursos(request): 
    return render(request, 'cursos.html')

def reconocimientos(request): 
    return render(request, 'reconocimientos.html')

def productos_academicos(request): 
    return render(request, 'productos_academicos.html')

def garage(request): 
    return render(request, 'garage.html')