from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral, Curso, ProyectoGarage, Habilidad, Reconocimiento

admin.site.register(DatosPersonales)
admin.site.register(ExperienciaLaboral)
admin.site.register(Curso)
admin.site.register(ProyectoGarage)
admin.site.register(Habilidad)
admin.site.register(Reconocimiento)