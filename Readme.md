# Marryme

Projeto feito com Django, Django Rest Framework e JWT.

#### Passo 1
> Criação de ambiente virtual
```bash
python3 -m venv .venv && source .venv/bin/activate
```

> Instalação das dependencias do projeto
```bash
python3 -m pip install -r dev-requirements.txt
```


#### Passo 2 - Instalação manual (caso não tenha seguido o passo anterior)
- Instalação do Django
```bash
pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install pymysql
pip install cryptography
```

#### Passo 3 - Iniciar projeto Django
```bash
django-admin startproject marryme .
python manage.py startapp budget
```

#### Passo 4 - SQL para criação do banco de dados
```bash
mkdir database
touch "01_create_database.sql"
```

```sql
CREATE DATABASE IF NOT EXISTS marryme_database;
USE marryme_database;
```

#### Passo 5 - Configuração do banco de dados

```python
# file: settings.py
import os
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "marryme_database",
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password"),
        "HOST": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "PORT": "3306",
    }
}
```

```python
# file: marryme/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```

#### Passo 6 - Imagem Docker e configuração com banco de dados mysql
```bash
docker build -t marryme-db .
docker run -d -p 3306:3306 --name=marryme-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=marryme_database marryme-db
```


#### Passo 7 - Executando as migrations e criando o superusuario
```bash
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py showmigrations
```

### Resetar imagem docker e migrations Django
```bash
docker ps # Para descobrir o ID do seu container com o banco de dados
docker stop <ID do seu container do banco> # Parar o container
docker remove <ID do seu container do banco> # Deletar o container
docker build -t seu-projeto-db .
docker run -d -p 3306:3306 --name=seu-projeto-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=seu-projeto_database marryme-db # Recriar o container
python3 manage.py migrate seu-app zero # Desfazer todas as migrations do app budget
rm seu-app/migrations/000* # Deletar a migration
python3 manage.py makemigrations # Recriar as migrations - agora com o campo user
python3 manage.py migrate # Efetuar as migrações para criar o banco
python3 manage.py createsuperuser # Recrie seu superuser

```


### Autenticações via Token

Ao optar por utilizar tokens no projeto, é necessário executar o comando de migrate, para que as tabelas de tokens sejam adicionadas no banco de dados do projeto.

```bash
# O ambiente virtual deve estar ativado
python manage.py migrate
```

Após a execução do comando acima, será criada a tabela `authtoken_token` no banco de dados