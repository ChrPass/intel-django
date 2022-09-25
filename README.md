# intel-django

This is an example project with django rest api

In order to use, installation of PostgreSQL is required
    sudo apt-get update
    sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

    if we don't have a db, we can create one with the following scripts
        sudo su - postgres
        psql
        CREATE DATABASE mydb;
        CREATE USER test WITH PASSWORD 'test';
        GRANT ALL PRIVILEGES ON DATABASE mydb TO test;
        \q
        exit


Create a db with 
Setting
    Create A Folder for the project
    Navigate into this folder
    Create environment to host your project
    Clone Project "git clone https://github.com/ChrPass/intel-django.git"
    For the environment we use virtualenv. TO install use sudo 'pip install virtualenv'.
    To create use "virtualenv env"
    To activate use "source env/bin/activate"
    navigate to project "cd intel-django"
    Install dependecies "pip3 freeze > requirements.txt"
    Make Migrations "python manage.py migrate"
    Add mock data to db with "python manage.py runscript load_terms"
    Run the app "python manage.py runserver"

