import os
from pathlib import Path
import dj_database_url

# 1. ESTA LÍNEA ES LA QUE FALTA O ESTÁ MAL UBICADA
BASE_DIR = Path(__file__).resolve().parent.parent

# ... resto de tu configuración (SECRET_KEY, DEBUG, etc.) ...

# 2. Asegúrate de que MEDIA_ROOT esté así después de definir BASE_DIR
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 3. Configuración para archivos estáticos (necesario para Render)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'