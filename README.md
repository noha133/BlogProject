# Blog Project

## Getting Started  
### Installing Dependencies  
#### Python   
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment  
I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies  

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies  
- [Django](https://www.djangoproject.com/)  is a backend framework. Django is required to handle requests and responses.

- [Django-rest-framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.


## Running the server  


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

To ensure the security of sensitive information, we've excluded the `.env` file from the Git repository. Follow these steps to set up the necessary environment variables:

## Create a .env file

1. Create a new file named `.env` in the root of your project.
2. Add the following content to the `.env` file, replacing placeholder values with your actual database credentials:

   ```env
   DB_ENGINE=your_db_engine
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
