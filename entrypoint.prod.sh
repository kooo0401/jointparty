#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 10
    # done

    echo "PostgreSQL started"
fi

# gunicornの起動・及びwebsocket通信の為のdaphne起動
# cd app && gunicorn --env DJANGO_SETTINGS_MODULE=jointparty.settings.production --bind 0.0.0.0:8000 jointparty.wsgi
python app/manage.py makemigrations
python app/manage.py migrate --noinput
python app/manage.py collectstatic --no-input --clear
# cd app && daphne -b 0.0.0.0 -p 8001 jointparty.asgi:application

exec "$@"