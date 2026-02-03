from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import never_cache

# Importamos xhtml2pdf para la generación de PDFs en el servidor
from xhtml2pdf import pisa 

from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

def get_contexto_comun():
    """Retorna el perfil principal para usar en todas las vistas."""
    return { 'perfil': Perfil.objects.first() }

# --- VISTAS DEL PORTAFOLIO ---

def home(request):
    context = get_contexto_comun()
    context['active_tab'] = 'inicio'
    
    if context['perfil']:
        # Cargamos los datos para las secciones de la página de inicio
        context['ultimos_proyectos'] = Proyecto.objects.all().order_by('-id')[:2]
        context['ultima_educacion'] = Educacion.objects.all().order_by('-fecha')[:2]
        context['ultima_experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')[:2]
        context['ultimos_certificados'] = Certificado.objects.all().order_by('-id')[:4]
        context['ultimos_productos'] = Producto.objects.filter(disponible=True)[:3]
        context['ultimos_cursos'] = Curso.objects.all().order_by('-fecha')[:3]
    
    return render(request, 'cv/home.html', context)

def experiencia(request):
    context = get_contexto_comun()
    context['active_tab'] = 'experiencia'
    context['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'cv/experiencia.html', context)

def educacion(request):
    context = get_contexto_comun()
    context['active_tab'] = 'educacion'
    context['productos_academicos'] = Educacion.objects.all().order_by('-fecha')
    return render(request, 'cv/educacion.html', context)

def proyectos(request):
    context = get_contexto_comun()
    context['active_tab'] = 'proyectos'
    context['proyectos'] = Proyecto.objects.all()
    return render(request, 'cv/proyectos.html', context)

def certificados(request):
    context = get_contexto_comun()
    context['active_tab'] = 'certificados'
    context['certificados'] = Certificado.objects.all()
    return render(request, 'cv/certificados.html', context)

def garage(request):
    context = get_contexto_comun()
    context['active_tab'] = 'garage'
    context['productos'] = Producto.objects.all()
    return render(request, 'cv/garage.html', context)

def cursos(request):
    context = get_contexto_comun()
    context['active_tab'] = 'cursos'
    context['cursos'] = Curso.objects.all().order_by('-fecha')
    return render(request, 'cv/cursos_lista.html', context)


# --- VISTA DE EXPORTACIÓN PDF ---

@xframe_options_exempt  # Necesario para mostrar el PDF en el iframe del modal
@never_cache            # Garantiza que el usuario siempre vea la versión más reciente
def descargar_cv_pdf(request):
    if request.method == 'POST':
        # 1. Captura de opciones del formulario
        ver_perfil = request.POST.get('incluir_perfil')
        ver_experiencia = request.POST.get('incluir_experiencia')
        ver_educacion = request.POST.get('incluir_educacion')
        ver_proyectos = request.POST.get('incluir_proyectos')
        ver_certificados = request.POST.get('incluir_certificados')
        accion = request.POST.get('action', 'download')

        # 2. Filtrado de datos según selección del usuario
        context = {}
        if ver_perfil: 
            context['perfil'] = Perfil.objects.first()
        if ver_experiencia: 
            context['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
        if ver_educacion: 
            context['educacion'] = Educacion.objects.all().order_by('-fecha')
        if ver_proyectos: 
            context['proyectos'] = Proyecto.objects.all()
        if ver_certificados: 
            context['certificados'] = Certificado.objects.all()

        # 3. Generación del HTML para el PDF
        html_string = render_to_string('cv/pdf_template.html', context)

        # 4. Configuración de la respuesta PDF
        response = HttpResponse(content_type='application/pdf')
        filename = "CV_Fernando_Exportado.pdf"

        if accion == 'preview':
            response['Content-Disposition'] = f'inline; filename="{filename}"'
        else:
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # 5. Creación del PDF mediante pisa
        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse('Error al generar el archivo PDF en el servidor.')
            
        return response

    return redirect('home')