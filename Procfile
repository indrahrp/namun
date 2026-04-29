web: cd catgallery && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn catsite.wsgi --bind 0.0.0.0:$PORT
