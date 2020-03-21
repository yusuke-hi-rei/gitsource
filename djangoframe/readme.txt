�� Install
  - Visual Studio Code
  - Django
�@  https://docs.djangoproject.com/ja/3.0/topics/install/#installing-official-release
  - Python  
    https://www.python.org/downloads/release/python-373/

1) python 3.7.3
   - Windows x86-64 executable installer
     �� Add Python 3.7 to PATH

2) Command prompt
   python -VER

3) Python �̉��z��
   python -m venv venv_private_diary

4) Python �̉��z���ɓ���/�ł�
   cd venv_private_diary\Scripts
   activate.bat
   deactivate

5) Django�C���X�g�[��(���z��)
   activate.bat
   (venv_private_diary) pip install django==2.2.2
   
6) PyCharm�C���X�g�[��(���z��)
   - download pycharm-community
   https://www.jetbrains.com/ja-jp/pycharm/download/
    
7) PostgreSQL�C���X�g�[��(���z��)
   v 10.12
   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

8) PostgreSQL���ϐ��ݒ�
   - �V�X�e�����ϐ��ݒ�

9) �f�[�^�x�[�X�쐬(���z��)
   (venv_private_diary) psql -U postgres
   
   (postgres=#) create database private_diary;
   
   �f�[�^�x�[�X�ꗗ: (postgres=#) \l
   ���O�A�E�g: (postgres=#) \q

10) psycopg2 PostgreSQL�ڑ��h���C�o�C���X�g�[��(���z��)
    (venv_private_diary) pip install psycopg2-binary






- Django project making.
  / django-admin startproject django_private


- Django application making.
  / cd django_private
  / python manage.py startapp django_private01

