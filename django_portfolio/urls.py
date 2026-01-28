from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('perfil/', views.perfil_view, name='perfil'),
    
    # Esta es la ruta que abrirá el diseño profesional en la pestaña nueva
    path('imprimir-cv/', views.imprimir_cv, name='imprimir_cv'), 
    
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('productos_academicos/', views.productos_academicos, name='productos_academicos'),
    path('garage/', views.garage, name='garage'),
]