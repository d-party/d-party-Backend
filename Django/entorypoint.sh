#!/bin/sh

if [ "$DEBUG" = 1 ]; then
    poetry run python manage.py runserver 0.0.0.0:8000
else
    # use uvicorn worker over the gunicorn
    # https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/uvicorn/
    # https://stackoverflow.com/questions/62543342/gunicorn-gevent-workers-vs-uvicorn-asgi
    poetry run gunicorn
fi