#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input # <--- ESTO ARREGLA EL DISEÑO
python manage.py migrate