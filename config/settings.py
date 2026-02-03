import os
from pathlib import Path
import dj_database_url

# --- 1. DEFINICIÓN DE RUTA BASE (ESTO FALTABA Y DABA ERROR) ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 2. SEGURIDAD ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-clave-secreta-por-defecto')

# En Render DEBUG será False. En tu PC será True.
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*']

# --- 3. APLICACIONES INSTALADAS (EL ORDEN ES CRUCIAL) ---
INSTALLED_APPS = [
    'cloudinary_storage',       # <--- OBLIGATORIO: Debe ir PRIMERO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # <--- OBLIGATORIO para el Admin
    'cv',                       # Tu aplicación
    'cloudinary',               # <--- OBLIGATORIO: Debe ir al FINAL
]

# --- 4. MIDDLEWARE (WHITENOISE AQUÍ ES VITAL) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <--- ESTO PINTA EL ADMIN DE AZUL
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

# --- 6. VALIDADORES DE CONTRASEÑA ---
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# --- 7. IDIOMA Y ZONA HORARIA ---
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# --- 8. ARCHIVOS ESTÁTICOS (CSS/JS - ESTO ARREGLA EL ADMIN) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Esta configuración activa la compresión de WhiteNoise para producción
# Sin esto, el Admin sale gris/roto en Render
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- 9. ARCHIVOS MEDIA (FOTOS - ESTO ARREGLA LAS FOTOS NEGRAS) ---
MEDIA_URL = '/media/'
# Esto le dice a Django: "Guarda las fotos en Cloudinary, no en el disco local"
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --- 10. TUS CREDENCIALES DE CLOUDINARY ---
# (Pon aquí tus claves reales que copiaste de cloudinary.com)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'TU_CLOUD_NAME',
    'API_KEY': 'TU_API_KEY',
    'API_SECRET': 'TU_API_SECRET',
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'