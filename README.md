# Unifying the Data from Various Health Sources

This project aims to unify the data of patients from different sources and store it in a centralized system. The admin has the authority to collaborate with pharmacies, clinics, and hospitals, allowing them to add patient details to this system. The authority is granted by the admin.

## Tech Stack

- Django (Python framework)

## Prerequisites

- Python should be installed on your system.

## Installation and Setup

Follow these steps to set up the project environment, create a new Django project, and create a Django app:

### 1. Install Python

Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

It is recommended to create a virtual environment for your project to manage dependencies:

```bash
# Install virtualenv if you don't have it already
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Django
Once the virtual environment is activated, install Django:

bash
pip install django
4. Create a New Django Project
Create a new Django project named taskmanager:

bash
django-admin startprojecttaskmanager
cd health_data_unifier
5. Create a New Django App
Create a new Django app named task:

bash
python manage.py startapp task
6. Configure the Django Project
Add the health app to your project's settings. Open health_data_unifier/settings.py and add 'health' to the INSTALLED_APPS list:

Python
INSTALLED_APPS = [
    ...
    'tasks',
]
7. Run Migrations
Apply the initial migrations to set up the database:

bash
python manage.py migrate
8. Create a Superuser
Create a superuser (admin) to manage the system:

bash
python manage.py createsuperuser
Follow the prompts to set up the admin user.

9. Run the Development Server
Start the Django development server:

bash
python manage.py runserver
You can now access the admin panel by navigating to http://127.0.0.1:8000/admin in your web browser and logging in with the superuser credentials.

Usage
The admin can collaborate with pharmacies, clinics, and hospitals to add patient details to the system. The admin grants authority to these entities to manage patient data.


 
 
