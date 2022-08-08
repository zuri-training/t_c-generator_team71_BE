web: gunicorn terms_gen_home.wsgi --log-file -
release: python manage.py makemigrattions --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput