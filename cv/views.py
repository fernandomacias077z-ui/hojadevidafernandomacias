from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import never_cache

# Importamos xhtml2pdf (la librería que funciona en Windows sin errores)
from xhtml2pdf import pisa 

from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

def get_contexto_comun():
    # Evita errores si aún no has creado un perfil en el admin
    return { 'perfil': Perfil.objects.first() }

# --- VISTAS NORMALES DE TU PÁGINA ---

def home(request):
    context = get_contexto_comun()
    context['active_tab'] = 'inicio'
    
    if context['perfil']:
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


# --- VISTA PDF INTELIGENTE (LA IMPORTANTE) ---

@xframe_options_exempt  # Permite que se vea dentro del IFRAME
@never_cache            # Evita que se quede pegado un PDF viejo
def descargar_cv_pdf(request):
    if request.method == 'POST':
        
        # 1. CAPTURAR QUÉ MÓDULOS QUIERE EL USUARIO
        ver_perfil = request.POST.get('incluir_perfil')
        ver_experiencia = request.POST.get('incluir_experiencia')
        ver_educacion = request.POST.get('incluir_educacion')
        ver_proyectos = request.POST.get('incluir_proyectos')
        ver_certificados = request.POST.get('incluir_certificados')

        # 2. CAPTURAR LA ACCIÓN (¿Preview o Download?)
        # Esto viene del input oculto "action" que manipulamos con JS en el home
        accion = request.POST.get('action', 'download')

        # 3. FILTRAR LA INFORMACIÓN PARA EL PDF
        context = {}
        if ver_perfil: context['perfil'] = Perfil.objects.first()
        if ver_experiencia: context['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
        if ver_educacion: context['educacion'] = Educacion.objects.all().order_by('-fecha')
        if ver_proyectos: context['proyectos'] = Proyecto.objects.all()
        if ver_certificados: context['certificados'] = Certificado.objects.all()

        # 4. RENDERIZAR LA PLANTILLA DEL PDF (pdf_template.html)
        html_string = render_to_string('cv/pdf_template.html', context)

        # 5. PREPARAR LA RESPUESTA HTTP
        response = HttpResponse(content_type='application/pdf')
        filename = "CV_Exportado.pdf"

        # --- AQUÍ ESTÁ LA LÓGICA CLAVE ---
        if accion == 'preview':
            # 'inline' le dice al navegador: "Muéstralo aquí mismo (en el iframe)"
            response['Content-Disposition'] = f'inline; filename="{filename}"'
        else:
            # 'attachment' le dice al navegador: "Descárgalo como archivo"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
        # ----------------------------------

        # 6. GENERAR EL PDF FINAL
        pisa_status = pisa.CreatePDF(html_string, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generando PDF. Revisa la consola.')
            
        return response

    # Si alguien intenta entrar directo por URL sin formulario, lo mandamos al inicio
    return redirect('home')