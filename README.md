# Unifying the Data from Various Health Sources

This project aims to unify the data of patients from different sources and store it in a centralized system. The admin has the authority to collaborate with pharmacies, clinics, and hospitals, allowing them to add patient details to this system. The authority is granted by the admin.

## Tech Stack

- Django (Python framework)

## Prerequisites

- Python should be installed on your system.

## Installation and Setup

Follow these steps to set up the project environment, create a new Django project, and create a Django app:

  **1. Install Python**
 Make sure Python is installed on your system. You can download it from
 
     [python.org](https://www.python.org/downloads/).

  **2. Create a Virtual Environment**: 
It is recommended to create a virtual environment for your project to manage dependencies:
  
 **Install virtualenv if you don't have it already**
     
     pip install virtualenv

**Create a virtual environment**
     
      py -m venv task_venv

**Activate the virtual environment**

**1. On Windows**: 

       task_venv\Scripts\activate

**2. On macOS/Linux**: 

      task_venv/bin/activate

**3. Install Django**(Once the virtual environment is activated, install Django): 

     pip install django

**4. Create a New Django Project**(Create a new Django project named taskmanager): 

     django-admin startproject taskmanager

**5. Change the directory**:(change the directory to the directory to the project directory that you have created)

     cd  taskmanager

**6. Create a New Django App**(Create a new Django app named task): 
      
      python manage.py startapp task

**7. Configure the Django Project**:
Add the health app to your project's settings. Open health_data_unifier/settings.py and add 'health' to the INSTALLED_APPS list:

Python


     INSTALLED_APPS = [
    ...
    'tasks',
     ]
**8. Run Migrations**(Apply the initial migrations to set up the database): 

     python manage.py migrate

 

**9. Create a Superuser**
(Create a superuser (admin) to manage the system): 

     python manage.py createsuperuser

Follow the prompts to set up the admin user.

**10. Run the Development Server**
(Start the Django development server):  

     python manage.py runserver

You can now access the admin panel by navigating to http://127.0.0.1:8000/admin in your web browser and logging in with the superuser credentials.

**Usage**
The admin can collaborate with pharmacies, clinics, and hospitals to add patient details to the system. The admin grants authority to these entities to manage patient data.

## OUTPUT

**ADMIN LOGIN**

 ![Screenshot 2025-01-10 135737](https://github.com/user-attachments/assets/70548d07-42d6-4850-b031-35d6cdf6e791)


**HOME PAGE**

![Screenshot 2024-12-14 151007](https://github.com/user-attachments/assets/4ecdb10f-185b-427b-9832-921f6625842b)


**ADDITION OF THE USERS**

![Screenshot 2024-12-14 151440](https://github.com/user-attachments/assets/d7822c43-92d0-433f-a174-a971baebdf61)


**PERMISSION GRANTING FOR THE USERS**

![Screenshot 2024-12-14 151650](https://github.com/user-attachments/assets/f974f0ac-226f-4471-b8a5-d2dd0ee0ada6)

