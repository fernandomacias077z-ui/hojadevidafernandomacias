from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Corregido: debe ser .urls
    path('admin/', admin.site.urls),
    
    # Conexión con tu aplicación 'tasks'
    path('', include('tasks.urls')),
]

# Configuración para servir archivos multimedia (fotos del Garage Tech)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)