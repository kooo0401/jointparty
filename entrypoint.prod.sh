#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# cd app && gunicorn jointparty.wsgi:application --bind 0.0.0.0:8000
# cd app && gunicorn --env DJANGO_SETTINGS_MODULE=jointparty.settings.production --bind 0.0.0.0:8000 jointparty.wsgi --error-logfile FILE
cd app && gunicorn --env DJANGO_SETTINGS_MODULE=jointparty.settings.production --bind 0.0.0.0:8000 jointparty.wsgi


exec "$@"