from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral, Curso, Reconocimiento, ProyectoGarage

admin.site.register(DatosPersonales)
admin.site.register(ExperienciaLaboral)
admin.site.register(Curso)
admin.site.register(Reconocimiento)
admin.site.register(ProyectoGarage)