from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'telefono')

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('puesto', 'empresa', 'periodo', 'estado') # Aquí verás el estado rápido
    list_filter = ('estado',) # Filtro para ver quién sigue activo
    search_fields = ('puesto', 'empresa')
