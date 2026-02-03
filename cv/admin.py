from django.contrib import admin
from django.utils.html import format_html # Necesario para mostrar las imágenes en el panel
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

# --- PERSONALIZACIÓN GLOBAL DEL ENCABEZADO ---
admin.site.site_header = "SISTEMA_ROOT_ADMIN"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Gestión de Portafolio"

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    # 'ver_foto' añade la miniatura a la lista principal
    list_display = ('nombre', 'apellido', 'profesion', 'ver_foto')
    search_fields = ('nombre', 'apellido', 'dni')

    def ver_foto(self, obj):
        """Genera una vista previa de la foto de perfil en el listado"""
        if obj.foto:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover;" />', obj.foto.url)
        return format_html('<span style="color: #999;">SIN_FOTO</span>')
    
    ver_foto.short_description = 'Imagen' # Título de la columna

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'ver_imagen')
    list_filter = ('perfil',)

    def ver_imagen(self, obj):
        """Genera una vista previa de la imagen del proyecto"""
        if obj.imagen:
            return format_html('<img src="{}" style="width: 60px; height: 40px; border-radius: 4px; object-fit: cover;" />', obj.imagen.url)
        return "-"
    
    ver_imagen.short_description = 'Preview'

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'estado', 'disponible')
    list_filter = ('estado', 'disponible')
    list_editable = ('precio', 'disponible') # Permite editar el precio sin entrar al registro

# --- REGISTRO DE LOS DEMÁS MODELOS ---
# Se registran de forma sencilla ya que no requieren previsualizaciones complejas
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Certificado)
admin.site.register(Curso)