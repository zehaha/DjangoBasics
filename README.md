# DCS-Website
=============

Django-based website for the Department of Computer Science in the University of the Philippines.

## Requirements

1. Python (see requirements.txt for details)
  * Django 1.6.4 - Web Framework
  * Pillow 2.4.0 - Images
  * South 1.0 - Database Migrations
  * argparse 1.2 - Django management via command-line interface
  * psycopg2 2.5 - PostgreSQL adapter for Python, requires libpq-dev and python-dev
  * wsgiref 0.1.2 - Web server for development
2. PostgreSQL (database)
3. libpq-dev (for connecting PostgreSQL to Python)
4. python-dev (for embedding Python in applications)
5.

## Setup
--------

### Django
Everything's in the tutorial :bd  
https://docs.djangoproject.com/en/1.6/intro/tutorial01/

### How to install PostgreSQL in Ubuntu and make it work with Django:
1. Install postgresql on your system. You may check the following links:
  * https://www.codefellows.org/blog/how-to-install-postgresql#ubuntu
  * https://help.ubuntu.com/community/PostgreSQL
2. Open psql as postgres

    ```
sudo -u postgres psql
    ```

3. Create the dcswebsite database

    ```sql
CREATE DATABASE dcswebsite;
    ```

4. Create a role named dcswebteam

    ```sql
CREATE ROLE dcswebteam WITH CREATEDB CREATEROLE CREATEUSER INHERIT LOGIN REPLICATION PASSWORD 'dcsw3bt3am';
    ```

5. Grant all privileges on database dcswebsite to role dcswebteam

    ```sql
GRANT ALL PRIVILEGES ON DATABASE dcswebsite TO dcswebteam;
    ```

6. Exit psql.

    ```sql
\q
    ```

7. Install libpq-dev and python-dev on your system

    ```
sudo apt-get install libpq-dev python-dev
    ```

8. Install psycopg2 on your virtual environment

    ```
pip install psycopg2
    ```

9. Edit DCS_Website/settings.py and replace the databases variable with:

    ```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcswebsite',
        'USER': 'dcswebteam',
        'PASSWORD': 'dcsw3bt3am',
        'HOST': 'localhost'
    }
}
    ```

## Running the server

### Local (wsgiref)
```
python manage.py runserver
```
