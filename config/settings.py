import os
from pathlib import Path
import dj_database_url

# --- 1. DEFINICIÓN DE RUTA BASE (ESTO ES LO QUE FALTABA) ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 2. SEGURIDAD ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-clave-secreta-por-defecto')

# DEBUG: False en Render (Producción), True en tu PC
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*']

# --- 3. APLICACIONES INSTALADAS ---
INSTALLED_APPS = [
    'cloudinary_storage',       # <--- IMPORTANTE: Debe ir PRIMERO para las fotos
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # <--- Necesario para WhiteNoise (Admin)
    'cv',
    'cloudinary',               # <--- IMPORTANTE: Debe ir al FINAL
]

# --- 4. MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # <--- OBLIGATORIO: Para que el Admin tenga estilo
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# --- 5. BASE DE DATOS ---
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# --- 6. VALIDACIÓN DE PASSWORD ---
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# --- 7. INTERNACIONALIZACIÓN ---
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# --- 8. ARCHIVOS ESTÁTICOS (CSS, JS, ADMIN) ---
# WhiteNoise se encarga de esto para que el Admin no se vea roto
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if not DEBUG:
    # Compresión y caché para producción
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- 9. ARCHIVOS MEDIA (FOTOS) ---
# Cloudinary se encarga de esto para que las fotos no se borren
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --- 10. CREDENCIALES CLOUDINARY ---
# Reemplaza con tus datos reales de Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dzg9enxez',
    'API_KEY': '355115651862625',
    'API_SECRET': 'xnm31aRIM7jVodKHwvsfJ4Y4MEE',
}

# Configuración ID por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'