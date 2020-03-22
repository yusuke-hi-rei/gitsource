■ Install
  - Django
　  https://docs.djangoproject.com/ja/3.0/topics/install/#installing-official-release
  - Python  
    https://www.python.org/downloads/release/python-373/

1) python 3.7.3
   - Windows x86-64 executable installer
     ■ Add Python 3.7 to PATH

2) Command prompt
   python -VER

3) Python の仮想環境
   python -m venv venv_private_diary

4) Python の仮想環境に入る/でる
   cd venv_private_diary\Scripts
   activate.bat
   deactivate

5) Djangoインストール(仮想環境)
   activate.bat
   (venv_private_diary) pip install django==2.2.2
   
6) PyCharmインストール(仮想環境)
   - download pycharm-community
   https://www.jetbrains.com/ja-jp/pycharm/download/
    
7) PostgreSQLインストール(仮想環境)
   v 10.12
   https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

8) PostgreSQL環境変数設定
   - システム環境変数設定

9) データベース作成(仮想環境)
   (venv_private_diary) psql -U postgres
   
   (postgres=#) create database private_diary;
   
   データベース一覧: (postgres=#) \l
   ログアウト: (postgres=#) \q

10) psycopg2 PostgreSQL接続ドライバインストール(仮想環境)
    (venv_private_diary) pip install psycopg2-binary

11) Djangoプロジェクト作成 (仮想環境)
    (venv_private_diary) django-admin startproject private_diary

12) Djangoアプリケーション作成 (仮想環境)
    cd django_private
　　(venv_private_diary) python manage.py startapp diary

13) PyCharmからプロジェクトフォルダ（private_diary）を開く

14) Djangoプロジェクトの仮想環境で使用するPythonを設定する。
　　PyCharm [File]- [settings] [Project Interpreter]
      [venv_private_diary\Scripts\python.exe]


