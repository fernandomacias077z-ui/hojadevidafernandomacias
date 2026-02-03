#!/usr/bin/env bash
set -o errexit

# Instalar librerías
pip install -r requirements.txt

# RECOLECTAR ESTÁTICOS (ESTO ARREGLA EL ADMIN EN RENDER)
python manage.py collectstatic --no-input

# Aplicar cambios en la base de datos
python manage.py migrate