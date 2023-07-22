# Event_app
Event app where you can participate into activities in your city.

# Prerequsites
You will need to install **pipenv**

# Instalation
Use this command to install **pipenv**: `pip install pipenv`


### Clone the project repository:
`git clone https://github.com/FFenrir/Event_app`<br>
`cd your/project`<br>
Make sure your terminal is showing project's folder.

# Activate the Virtual Environment

`pipenv shell`<br>
After running the `pipenv shell` command, you will enter the virtual environment.

### Install project dependencies from the requirements.txt file using pipenv:

`pipenv install -r requirements.txt`<br>
This command will install the required packages from the requirements.txt file. It ensures that your project's dependencies are isolated within the virtual environment.


# Migrate the Database

`python manage.py migrate`<br>
This will apply the database migrations and set up the database schema.

## Create a Superuser

`python manage.py createsuperuser`<br>
This command will prompt the user to provide a Email, and Password for the superuser.


## Run the Development Server

`python manage.py runserver`<br>
The development server should now be running at http://127.0.0.1:8000/. Users can access your Django REST API using this URL.


## Go to admin panel
Use this url (http://127.0.0.1:8000/admin)<br>
Use your credentials that you used to create superuser.
