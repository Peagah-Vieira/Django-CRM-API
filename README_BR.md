# Django Customer Relationship Management

Uma API REST para [Django-CRM](https://github.com/Peagah-Vieira/Django-CRM).

## Funcionalidades

- Autenticação JSON Web Token com JWT

- Endpoints para cada aplicativo

- Documentação da API REST com Swagger

## Executando localmente

Clone o projeto

```bash
git clone  https://github.com/Peagah-Vieira/Django-CRM-API
```

Crie um ambiente virtual

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

Atualize o pip

```bash
py -m pip install --upgrade pip
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Alterar variáveis ​​de ambiente

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

Realize as migrações

```bash
py manage.py migrate
```

Iniciar o servidor

```bash
py manage.py runserver
```

## Aprendizados

Documentação da API REST:

(https://www.django-rest-framework.org/topics/documenting-your-api/)

Autenticação do JSON Web Token:

(https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Documentação

[Python](https://www.python.org)

[Django](https://www.djangoproject.com)

[Swagger](https://django-rest-swagger.readthedocs.io/en/latest/)

[Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
