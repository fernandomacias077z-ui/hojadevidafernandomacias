from django.shortcuts import render
from .models import DatosPersonales, ExperienciaLaboral, Curso, ProyectoGarage, Habilidad, Reconocimiento

def home(request):
    """Vista principal con contadores estadísticos."""
    return render(request, 'home.html', {
        'total_cursos': Curso.objects.count(),
        'total_proyectos': ProyectoGarage.objects.count(),
        'total_experiencia': ExperienciaLaboral.objects.count(),
    })

def perfil(request):
    """
    Panel de control profesional. 
    Incluye 'reconocimientos' para la lógica de personalización del PDF.
    """
    datos = DatosPersonales.objects.first() 
    experiencias = ExperienciaLaboral.objects.all().order_by('-fecha_inicio')[:2] 
    habilidades = Habilidad.objects.all()
    cursos = Curso.objects.all().order_by('-id')
    
    # Esta variable permite que la formación aparezca en el PDF
    reconocimientos = Reconocimiento.objects.all().order_by('-fecha_inicio')

    return render(request, 'perfil.html', {
        'datos': datos,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'cursos': cursos,
        'reconocimientos': reconocimientos  # Enviado correctamente al template
    })

def experiencia(request):
    """Vista detallada de la trayectoria laboral."""
    exp = ExperienciaLaboral.objects.all().order_by('-fecha_inicio')
    return render(request, 'experiencia.html', {'experiencias': exp})

def cursos(request):
    """Vista de certificaciones obtenidas."""
    curs = Curso.objects.all().order_by('-id') 
    return render(request, 'cursos.html', {'cursos': curs})

def reconocimientos(request):
    """Vista de formación académica y méritos."""
    reco = Reconocimiento.objects.all().order_by('-fecha_inicio')
    return render(request, 'reconocimientos.html', {'reconocimientos': reco})

def garage(request):
    """Vista de proyectos personales."""
    proyectos = ProyectoGarage.objects.all().order_by('-id')
    return render(request, 'garage.html', {'proyectos': proyectos})

def imprimir_cv(request):
    """
    Vista opcional para impresión directa mediante parámetros GET.
    Útil si decides usar una página de impresión dedicada en lugar del modal JS.
    """
    quiere_datos = request.GET.get('incluir_datos') == 'on'
    quiere_exp = request.GET.get('incluir_exp') == 'on'
    quiere_hab = request.GET.get('incluir_hab') == 'on'
    quiere_reco = request.GET.get('incluir_reco') == 'on'

    datos = DatosPersonales.objects.first() if quiere_datos else None
    experiencias = ExperienciaLaboral.objects.all().order_by('-fecha_inicio') if quiere_exp else []
    habilidades = Habilidad.objects.all() if quiere_hab else []
    reconocimientos = Reconocimiento.objects.all().order_by('-fecha_inicio') if quiere_reco else []

    return render(request, 'imprimir_cv.html', {
        'datos': datos,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'reconocimientos': reconocimientos,
    })