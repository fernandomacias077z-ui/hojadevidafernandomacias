from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Secciones del CV
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('certificados/', views.certificados, name='certificados'),
    path('cursos/', views.cursos, name='cursos'),
    
    # Tienda / Garage
    path('garage/', views.garage, name='garage'),
    
    # Generador de PDF Inteligente (Vista previa y Descarga)
    path('descargar-cv/', views.descargar_cv_pdf, name='descargar_cv_pdf'),
]