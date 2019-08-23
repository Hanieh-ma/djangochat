1. Install virtualenv
    * Linux: virtualenv <venvname>
    * Windows: virtualenv <venvname>
1.1 Install Django
    * pip install django    
2. Active virtualenv
    * Linux: source <venvname>/bin/activate
    * Windows: <venvname>\Scripts\activate.bat
    (<venvname>)
3. Create a project
    * django-admin startproject <projectname>
3.1 Change directory
    * cd <projectname>
4. Create an app
    * python manage.py startapp <appname>
5. Run django web server
    * python manage.py runserver
