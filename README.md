# Cupcake
A REST JSON API for cupcake info.<br/>
We used SQLAlchemy to communicate with our database.<br/>

## Technologies
* Python 3.7
* blinker 1.4
* certifi 2018.11.29
* chardet 3.0.4
* Click 7.0
* Flask 1.0.2
* Flask-DebugToolbar 0.10.1
* Flask-SQLAlchemy 2.3.2
* Flask-WTF 0.14.2
* idna 2.8
* itsdangerous 1.1.0
* Jinja2 2.10
* MarkupSafe 1.1.1
* psycopg2-binary 2.7.7
* requests 2.21.0
* SQLAlchemy 1.2.18
* urllib3 1.24.1
* Werkzeug 0.14.1
* WTForms 2.2.1

## To run the app on local

Set up folder:
```
 git clone git@github.com:ivyc81/Flask_Cupcake.git
 cd Flask_Cupcake
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```

Set up database:
```
createdb cupcakes-app
python seed.py
```

Start app:
```
 flask run # Open browser to localhost:5000 and try the app out!
```

## To run tests
```
createdb cupcakes-app-test
python -m unittest test_file_name
```
