#!/bin/sh

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    echo "Apply database migrations"
    python3 /app/manage.py migrate --noinput
fi

if [ "x$DJANGO_COLLECT_STATIC" = 'xon' ]; then
    echo "Collect static files"
    python3 /app/manage.py collectstatic --noinput
fi

exec "$@"
