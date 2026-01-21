# settings.py
LOGIN_URL = 'signin'
LOGIN_REDIRECT_URL = 'profile_cv'
LOGOUT_REDIRECT_URL = 'home'

# Para el PDF y fotos de proyectos
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'