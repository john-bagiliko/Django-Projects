# Django-Projects
This django app allows all to add a school, view a school, 
delete a school and  modify a school. One can 
make an api request and will have the ability to do anything with
 it, ie. GET, PUT, PATCH, DELETE etc.

This was done with django 2.0.

Install this version of django using:

$pip install Django==2.0.5

 I also created the a rest api for it using the django rest_framework.

Install the django rest_framwork using:

$pip install djangorestframework

Or

go to Django Rest framework page
http://www.django-rest-framework.org/
and follow the instructions.
 
I am also using MySQL database instead of the default sqlite database that 
comes with django.

If you want to use this database too, 
visit this place and have MySQL installed
https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial

Create your database:
as

mysql> CREATE DATABASE database_name;

Clone the repository into your directory as:

$cd your_directory


$git clone https://github.com/john-bagiliko/Django-Projects.git

Open the settings.py file and change "githubdb" to "database_name" 
under the DATABASES section

It should be something like 

DATABASES = {

	'default': {

		'ENGINE': 'django.db.backends.mysql',

		'NAME': 'database_name',

		'USER': 'root', #If your mysql username is different, replace 'root' with that.

		'PASSWORD': '', #you may need to put your password if you need it to login into you mysql database.


		'HOST': '',

		'PORT': '',
	}
}


However, if you would like to go with the default sqlite database, 

change the DATABASE section in the settings.py to look like this:

DATABASES = {

	'defaults': {

		'ENGINE': 'django.db.backends.sqlite3'),

		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

	}

} 

$cd Django-Projects/MySchool

$python manage.py migrate

$python manage.py makemigrations

$python manage.py migrate

$python manage.py createsuperuser

$python manage.py runserver 5000

go to your browser and type 

 http://127.0.0.1:5000/school
 
You can also visit the admin page using

http://127.0.0.1:5000/admin

and enter the details that you used when you run python manage.py createsuperuser

Let me know if it worked for you.
