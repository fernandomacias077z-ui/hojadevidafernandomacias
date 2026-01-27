from django.shortcuts import render

def home(request):
    context = {
        'nombre': 'Bruno Fernando Macias Moreira',
        'perfil': 'Bachiller en Informática y profesional de servicio con alta capacidad de trabajo bajo presión y resolución técnica.',
        'ubicacion': 'Jocay j4 y j9, Manta, Ecuador',
        'telefono': '0980643265',
        'email': 'Franyo678@gmail.com'
    }
    return render(request, 'home.html', context)

# Vistas simples que solo cargan el template correspondiente
def perfil_view(request):
    return render(request, 'perfil.html')

def experiencia(request): 
    return render(request, 'experiencia.html')

def cursos(request): 
    return render(request, 'cursos.html')

def reconocimientos(request): 
    return render(request, 'reconocimientos.html')

def productos_academicos(request): 
    return render(request, 'productos_academicos.html')

def garage(request): 
    return render(request, 'garage.html')