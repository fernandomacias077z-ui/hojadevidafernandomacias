import os
from pathlib import Path
import dj_database_url

# --- 1. RUTA BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 2. SEGURIDAD ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-prod-key-123')
DEBUG = 'RENDER' not in os.environ 
ALLOWED_HOSTS = ['*']

# --- 3. APPS INSTALADAS ---
INSTALLED_APPS = [
    'cloudinary_storage',       # Debe ir primero para interceptar fotos
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Necesario para WhiteNoise
    'cv',
    'cloudinary',               # Debe ir al final
]

# --- 4. MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ESTO ARREGLA EL ADMIN GRIS
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

# --- 5. BASE DE DATOS ---
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# --- 6. ARCHIVOS ESTÁTICOS (ADMIN / CSS) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- 7. ARCHIVOS MEDIA (FOTOS / CLOUDINARY) ---
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# REEMPLAZA ESTO CON TUS CLAVES DE CLOUDINARY.COM
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'TU_CLOUD_NAME',
    'API_KEY': 'TU_API_KEY',
    'API_SECRET': 'TU_API_SECRET',
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'