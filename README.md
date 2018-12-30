# Django-Projects
This django app allows all to add a school, view a school, 
delete a school, search a school and  modify a school. One can 
make an api request and will have the ability to do anything with
 it, ie. GET, PUT, PATCH, DELETE etc.

This was done with django 2.0.

Install this version of django using:


```bash
$pip install Django==2.0.5
```
 I also created the a rest api for it using the django rest_framework.

Install the django rest_framwork using:

$pip install djangorestframework

Or

go to Django Rest framework page
http://www.django-rest-framework.org/
and follow the installation instructions.
 
I am also using MySQL database instead of the default sqlite database that 
comes with django.

If you want to use this database too, 
visit this place and have MySQL installed
https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial

Create your database:
that is,
login to mysql and create a database using: 


```mysql
mysql> CREATE DATABASE database_name;
``` 

Note: Replace 'database_name' with your prefared name.

Now that your database is set, do

quit the database server using Ctrl + D

$mkdir your_directory

$ cd your_directory

Clone the repository into your directory as:

$git clone https://github.com/john-bagiliko/Django-Projects.git

Open the settings.py file in the project directory with a text editor

Verify that the DATABASES section looks something like this: 

```python

DATABASES = {

	'default': {

		'ENGINE': 'django.db.backends.mysql',

		'NAME': 'database_name', #replace 'database_name' with the name of the database you created

		'USER': 'root', #If your mysql username is different, replace 'root' with that.

		'PASSWORD': '', #you may need to put your password if you need it to login into you mysql database.


		'HOST': '',

		'PORT': '',
	}
}
```

However, if you would like to go with the default sqlite database instead,
just do the following:
```bash
$mkdir your_directory

$cd your_directory

$git clone https://github.com/john-bagiliko/Django-Projects.git
```
Open the settings.py file with a text editor and 

change the DATABASE section to look like this:

```python
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

You do not have to add anything else. This is fine for sqlite. Django will create the necessary database and all the tables 
required in this database. 

All is set! 

Whether using mysql or going with sqlite, lets all continue as follows:

```bash
$cd Django-Projects/MySchool
```

Perform the migrations to create tables in your database using:

```bash
$python manage.py migrate
```

Create an admin using: 


```bash
$python manage.py createsuperuser
```

Make migrations using:


```bash
$python manage.py makemigrations 
```

Finally, migrate


```bash
$python manage.py migrate
```

Run the development server using

$python manage.py runserver 5000

go to your browser and type 

 http://127.0.0.1:5000/school
 
 Access the api page on this link 
 
 http://127.0.0.1:5000/school/api/schools
 
 
You can also visit the admin page using

http://127.0.0.1:5000/admin

and enter the details that you used when you ran 'python manage.py createsuperuser'

Let me know if it worked for you.

email: john.bagiliko@aims-senegal.org
