#Django is a high-level web framework written in Python that allows developers to build secure, scalable, and maintainable web applications quickly.
#to start we first install it:
pip install django
#then we make a project
django-admin startproject (name of the projects)
#the file: manage.py s a command-line utility that Django creates automatically when you start a new project
#It helps you interact with your Django project easily — without typing long commands every time.
#now if we run
python manage.py runserver
#it gives us a link of our now locally run website
#now django helps us divide our website or application into multiple parts called apps
#A Django project (like your pyshop) is made up of one or more apps.
#Each app is a modular piece of your project that handles a specific feature or function.
#with the python manage.py startapp (name of the product) we can make a new app
#inside the app there are multiple files:
#admin: is used to administer your app
#the apps is used to store config settings for the app
#models is where we define classes and new types and concepts
#tests is where we write automated test for the app
#view is where we difine what the user should see when they navigate to a certain page