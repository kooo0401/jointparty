#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -zv $DATABASE_HOST $DATABASE_PORT
    do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python app/manage.py flush --no-input
python app/manage.py migrate
python app/manage.py collectstatic --no-input --clear

exec "$@"