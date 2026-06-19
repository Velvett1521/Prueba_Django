#!/bin/bash
# Script que ejecuta Vercel en el build
pip install -r requirements.txt --quiet
python manage.py collectstatic --no-input
