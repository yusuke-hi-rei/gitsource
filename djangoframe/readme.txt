�� Install
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

11) Django�v���W�F�N�g�쐬 (���z��)
    (venv_private_diary) django-admin startproject private_diary

12) Django�A�v���P�[�V�����쐬 (���z��)
    cd django_private
�@�@(venv_private_diary) python manage.py startapp diary

13) PyCharm����v���W�F�N�g�t�H���_�iprivate_diary�j���J��

14) Django�v���W�F�N�g�̉��z���Ŏg�p����Python��ݒ肷��B
�@�@PyCharm [File]- [settings] [Project Interpreter]
      [venv_private_diary\Scripts\python.exe]


