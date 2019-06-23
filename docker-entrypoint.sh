#!/bin/sh
set -e

>&2 echo "$DATABASE_URL"
until psql $DATABASE_URL -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done


if [ "$1" = 'gunicorn' ]; then
    >&2 echo "Executing migration"
    python manage.py migrate
fi

if [ "x$DJANGO_LOAD_INITIAL_DATA" = 'xon' ]; then
	/venv/bin/python manage.py load_initial_data
fi

exec "$@"
