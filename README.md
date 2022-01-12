# app-drf

## installation

```bash
% cd /path/to/app-drf
% pyenv install 3.7.12 2.7.18
% pyenv local 3.7.12
% python -m venv .venv
% pip install --upgrade pip
% pip install --upgrade setuptools
% pip install -r requirements.txt
% echo "DEBUG=True" > .env
% python manage.py migrate
% python manage.py createsuperuser
Username (leave blank to use 'pasta'): admin
Email address: admin@example.com
Password: admin
Password (again): admin
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## running

```bash
% source .venv/bin/activate
% python manage.py runserver
```

## debug

```bash
% python manage.py runserver_plus
```

```bash
% python manage.py shell
```

## memo

```bash
pip install flake8 black mypy
pip install Django
pip install python-dotenv django-extensions Werkzeug django-debug-toolbar django-security
pip install djangorestframework markdown django-filter
pip install pygments
pip install pytest pytest-mock
pip install Cerberus
pip install gunicorn ptvsd
```
