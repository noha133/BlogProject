# Blog Project

## Getting Started  
### Installing Dependencies  
#### Python   
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment  
I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies  
Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies  
- [Django](https://www.djangoproject.com/)  is a backend framework. Django is required to handle requests and responses.

- [Django-rest-framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.


## Running the server  
From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:
#### Mac , Linux

```bash

python3 manage.py runserver
```

To run the server, execute:
#### Windows

```bash
python manage.py runserver
```
## Install a Database

### For MySQL Users:

1. Go to the [MySQL Downloads](https://dev.mysql.com/downloads/mysql/) page.
2. Download the MySQL Community Server installer based on your operating system.
3. Run the installer and follow the setup instructions.

### For PostgreSQL Users:

1. Go to the [PostgreSQL Downloads](https://www.postgresql.org/download/) page.
2. Download the PostgreSQL installer based on your operating system.
3. Run the installer and follow the setup instructions.

## Create a Local Database

### For MySQL Users:

1. Open a terminal or MySQL command line.
2. Log in to MySQL using your username and password.
3. Create a new database for [Your Project Name]:

   ```sql
   CREATE DATABASE your_project_name;
