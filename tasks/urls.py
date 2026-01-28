from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('curriculum/', views.imprimir_cv, name='imprimir_cv'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('garage/', views.garage, name='garage'),
    # Verificamos que este nombre coincida con la función en views.py
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
]