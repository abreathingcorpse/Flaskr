# Flaskr
Flask tutorial App

You'll need to create your own virtual environment with:

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install Flask
```

For more info, check out:
https://flask.palletsprojects.com/en/3.0.x/installation/

In order to run the Hello World App, you'll need to activate
your python venv and then run the flask binary with the app as
an argument:
```
$ source .venv/bin/activate
$ flask --app hello run
```

You'll find your app within the following URL, which you may
access throughout any Web Browser:
http://127.0.0.1:5000/

For more info, check out:
https://flask.palletsprojects.com/en/3.0.x/quickstart/


In order to run the flaskr App, you'll need to activate your
python venv and then run the flask binary with the app as
an argument: 
```
$ source .venv/bin/activate
$ flask --app flaskr run --debug
```

You'll find your app within the following URL, which you may
access throughout any Web Browser:
http://127.0.0.1:5000/hello

For more info, check out:
https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/

In order to initialize your Database File you'll need to
activate your python venv and then run the flask command with
`init-db` as argument instead of run:
```
$ source .venv/bin/activate
$ flask --app flaskr init-db
```