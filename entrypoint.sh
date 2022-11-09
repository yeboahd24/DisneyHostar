#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn DisneyPlusClone.wsgi:application --bind 127.0.0.1:7000

# update to new requirements on each container start
pip --no-cache-dir install --upgrade -r requirements.txt