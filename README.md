# jollyjango

# how do you start generating a new project, when your directory is blank
```commandline
django-admin startproject project_name_here
```

# file starter during the boilerplate
- __init__.py: treat directory like a python package
- asgi.py: special config files that we do not need to deal with
- wsgi.py: special config files that we do not need to deal with
- settings.py: we will visit this file to install different applications, install plugins and change db engine
- urls.py: different url routes, to route to different django applcation
- manage.py command line tool, to run special commands, like example make database migrations or run the web server

# how do you create your myapp directory
```commandline
python maange.py startapp name_of_app_here
```

# how to link the app with the django project
1. go to th manage.py, put the folder myapp into the installed app variables like the example below.
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp"
]
```

# how do you start running the server
```commandline
python manage.py runserver
```

# what is the template in django ?
a template is a reusable HTML file that you can use to dynamically display HTML data.
# what are blocks in templates in django ?
blocks are contents that a parameterised and override to be able to show new content

# everytime, u make changes to the database, u have to run migrations to apply the changes
```commandline
python manage.py makemigrations
```

# how do you create your superuser
```commandline
python manage.py createsuperuser
```