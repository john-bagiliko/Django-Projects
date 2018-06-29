# Django-Projects
This django app allows all to add a school, view a school, 
delete a school and  modify a school. Anybody can 
make an api request and will have the ability to do anything with it.
There are no securtiy measures in place for now.

This was done with django 2.0.
 I also created the a rest api for it using the django rest_framework.

To test this app, go to Django Rest framework site
http://www.django-rest-framework.org/
and follow the instructions.

Use 
$ pip install Django==2.0.5 

to have django installed

I am also using MySQL database instead of the default sqlite database that 
comes with django.

Visit this place and have MySQL installed
https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial

Create your database:
as

mysql> CREATE DATABASE database_name;

Clone the repository into your directory as:

$cd your_directory
$git clone https://github.com/john-bagiliko/Django-Projects.git

Open the settings.py file and change "githubdb" to "database_name" 
under the DATABASES section

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
