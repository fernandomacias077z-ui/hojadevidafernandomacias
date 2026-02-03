#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input # <--- ESTO ARREGLA EL ADMIN
python manage.py migrate