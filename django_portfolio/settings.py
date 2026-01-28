import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: Usa variable de entorno en Render, o la clave insegura en local
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-bruno-key')

# DEBUG: False en Render, True en local
DEBUG = 'RENDER' not in os.environ 

# ALLOWED_HOSTS: Permitir el dominio de Render y local
ALLOWED_HOSTS = ['*']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Debe ir aquí para los estilos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_portfolio.urls'

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

WSGI_APPLICATION = 'django_portfolio.wsgi.application'

# BASE DE DATOS: SQLite en local, PostgreSQL en Render (si configuras la URL)
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# ARCHIVOS ESTÁTICOS (CSS, JS, IMÁGENES)
STATIC_URL = '/static/'

# Dónde buscar archivos en desarrollo
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Dónde se reunirán todos para producción (Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración específica de WhiteNoise para producción
if not DEBUG:
    # Usamos CompressedStaticFilesStorage para evitar errores de manifest faltante
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'