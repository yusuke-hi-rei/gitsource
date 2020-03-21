- Install
  - Django
@  https://docs.djangoproject.com/ja/3.0/topics/install/#installing-official-release
  - Visual Studio Code
    
  - python 3.7.6

  - Django install(3.0.4)
  / python -m pip install Django
-------------------------------------------------------
>python -m pip install Django
Collecting Django
  Downloading Django-3.0.4-py3-none-any.whl (7.5 MB)
     |????????????????????????????????| 7.5 MB 3.3 MB/s
Requirement already satisfied: pytz in c:\users\yultu\anaconda3\lib\site-packages (from Django) (2019.3)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
     |????????????????????????????????| 40 kB 2.6 MB/s
Collecting asgiref~=3.2
  Downloading asgiref-3.2.5-py2.py3-none-any.whl (19 kB)
Installing collected packages: sqlparse, asgiref, Django
Successfully installed Django-3.0.4 asgiref-3.2.5 sqlparse-0.3.1
----------------------------------------------------------------

- Django project making.
  / django-admin startproject django_private


- Django application making.
  / cd django_private
  / python manage.py startapp django_private01

