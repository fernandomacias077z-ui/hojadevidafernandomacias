from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

# --- PERSONALIZACIÓN DEL ADMIN ---
admin.site.site_header = "Admin"
admin.site.site_title = "Panel de Admin"
admin.site.index_title = "Panel de Control"

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'profesion')
    search_fields = ('nombre', 'apellido', 'dni')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'perfil', 'fecha_inicio')
    list_filter = ('perfil',) # Filtro lateral para ver experiencias por perfil

@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'perfil', 'fecha')
    list_filter = ('perfil',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'perfil', 'fecha')
    list_filter = ('perfil',)

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'perfil', 'fecha')
    list_filter = ('perfil',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'estado', 'perfil', 'disponible')
    list_filter = ('perfil', 'estado')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'perfil', 'ver_pdf')
    list_filter = ('perfil',)
    search_fields = ('titulo', 'descripcion')
    
    def ver_pdf(self, obj):
        return "Sí" if obj.pdf_archivo else "No"
    ver_pdf.short_description = "¿Tiene PDF?"