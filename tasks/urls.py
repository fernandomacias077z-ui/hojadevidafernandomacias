from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('imprimir-cv/', views.imprimir_cv, name='imprimir_cv'),
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('trayectoria/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('garage/', views.garage, name='garage'),
]