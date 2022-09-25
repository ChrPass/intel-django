# intel-django

This is an example project with django rest api

In order to use, installation of PostgreSQL is required<br />
    sudo apt-get update<br />
    sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib<br />

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
    Create A Folder for the project<br />
    Navigate into this folder<br />
    Create environment to host your project<br />
    Clone Project "git clone https://github.com/ChrPass/intel-django.git"<br />
    For the environment we use virtualenv. TO install use sudo 'pip install virtualenv'.<br />
    To create use "virtualenv env"<br />
    To activate use "source env/bin/activate"<br />
    navigate to project "cd intel-django"<br />
    Install dependecies "pip3 freeze > requirements.txt"<br />
    Make Migrations "python manage.py migrate"<br />
    Add mock data to db with "python manage.py runscript load_terms"<br />
    Run the app "python manage.py runserver"<br />

