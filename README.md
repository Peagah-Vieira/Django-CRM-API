[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Peagah-Vieira/Django-CRM-API/blob/main/README_BR.md)
[![Python 3.11](https://img.shields.io/badge/python-3.11-yellow.svg)](https://www.python.org/downloads/release/python-360/)
![Django 4.2](https://img.shields.io/badge/Django-4.2-green.svg)
# Django Customer Relationship Management - API

A REST API for [Django-CRM](https://github.com/Peagah-Vieira/Django-CRM).

## Functionalities

- JSON Web Token authentication with JWT

- Endpoints for each app

- REST API documentation with Swagger

## Running locally

Clone the project

```bash
git clone  https://github.com/Peagah-Vieira/Django-CRM-API
```

Create a virtual environment

```bash
# Linux
sudo apt-get install python3-venv    
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

Update the pip

```bash
py -m pip install --upgrade pip
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Change environment variables

```bash
# Django Configuration
# SECRET_KEY = 'GENERATE A KEY'

# JWT Configuration
# JWT_SECRET_KEY = 'GENERATE A KEY'

# PostgreSQL Local Configuration
# DB_ENGINE = 'django.db.backends.postgresql'
# POSTGRES_DB = "CHANGE-ME"
# POSTGRES_USER = "CHANGE-ME"
# POSTGRES_PASSWORD = "CHANGE-ME"
# POSTGRES_HOST = "127.0.0.1"
# POSTGRES_PORT = "5432"
```

Perform the migrations

```bash
py manage.py migrate
```

Start the server

```bash
py manage.py runserver
```

## Learnings

REST API documentation:

(https://www.django-rest-framework.org/topics/documenting-your-api/)

JSON Web Token authentication:

(https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Documentation

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)

[Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
