#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput
sleep 15
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# create a superuser
export DJANGO_SUPERUSER_PASSWORD=gregncl
export DJANGO_SUPERUSER_USERNAME=greg
export DJANGO_SUPERUSER_EMAIL=greg@somewhere.ac.uk

python manage.py createsuperuser --noinput 

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
