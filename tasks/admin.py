from django.contrib import admin
from .models import DatosPersonales

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información de Sistema', {
            'fields': ('idperfil', 'descripcionperfil', 'perfilactivo')
        }),
        ('Datos de Identidad', {
            'fields': (('nombres', 'apellidos'), ('numerocedula', 'fechanacimiento'), ('nacionalidad', 'lugarnacimiento'))
        }),
        ('Información Personal', {
            'fields': (('sexo', 'estadocivil', 'licenciaconducir'),)
        }),
        ('Contacto', {
            'fields': (('telefonoconvencional', 'telefonofijo'), 'direcciondomiciliaria', 'direcciontrabajo', 'sitioweb')
        }),
    )
    list_display = ('nombres', 'apellidos', 'numerocedula', 'perfilactivo')