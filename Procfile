web: gunicorn --pythonpath mysite mysite.wsgi
heroku ps: scale web=1
release: cd mysite && python manage.py createsuperuser