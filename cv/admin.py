from django.contrib import admin
from django.utils.html import format_html
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

admin.site.site_header = "SISTEMA_ROOT_ADMIN"

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'profesion', 'ver_foto')
    
    def ver_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />', obj.foto.url)
        return "SIN_FOTO"
    ver_foto.short_description = 'Imagen'

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'ver_imagen')
    
    def ver_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 60px; height: 40px; border-radius: 4px;" />', obj.imagen.url)
        return "-"

admin.site.register([Experiencia, Educacion, Certificado, Producto, Curso])