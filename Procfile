release: python manage.py migrate && python manage.py deleteAll && python manage.py seed
web: gunicorn TheIndex.wsgi --log-file -
