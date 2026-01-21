# Busca estas líneas y asegúrate de que NO estén comentadas o borradas:

ROOT_URLCONF = 'django_portfolio.urls' # <--- ESTA ES LA QUE FALTA SEGÚN EL LOG

WSGI_APPLICATION = 'django_portfolio.wsgi.application'

# También revisa que estas sigan ahí para que cargue tus 8 archivos HTML:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Asegúrate de que apunte a tu carpeta de templates
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