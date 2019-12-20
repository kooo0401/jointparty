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
# cd app && gunicorn --env DJANGO_SETTINGS_MODULE=jointparty.settings.production --bind 34.84.99.154:80 jointparty.wsgi

docker-compose -f docker-compose.prod.yml exec django python app/manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec django python app/manage.py collectstatic --no-input --clear


exec "$@"