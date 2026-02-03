import os
# ... (otras importaciones)

# 1. APLICACIONES INSTALADAS
INSTALLED_APPS = [
    'cloudinary_storage', # <--- IMPORTANTE: Al principio
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # <--- Asegúrate de que esto esté aquí
    'cv',
    'cloudinary', # <--- IMPORTANTE: Al final
]

# 2. MIDDLEWARE (Revisa que WhiteNoise esté aquí)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # <--- OBLIGATORIO PARA QUE EL ADMIN SE VEA BIEN
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... resto del archivo ...

# 3. CONFIGURACIÓN HÍBRIDA (La solución definitiva)

# A) ARCHIVOS ESTÁTICOS (CSS, JS, ADMIN) -> Usan WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Esta línea es la que hace que el Admin funcione en Render:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# B) ARCHIVOS MEDIA (Tus fotos subidas) -> Usan Cloudinary
MEDIA_URL = '/media/'
# Esta línea es la que hace que tus fotos no se borren:
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# C) TUS CREDENCIALES DE CLOUDINARY (No las borres)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'PON_AQUI_TU_CLOUD_NAME',
    'API_KEY': 'PON_AQUI_TU_API_KEY',
    'API_SECRET': 'PON_AQUI_TU_API_SECRET',
}