fire_api
========

simple flask REST api to grab and regurgitate USFS major fires CSV

get the app:
```abenrob$ git clone https://github.com/abenrob/fire_api.git```

set up the virtual environment (need [virtualenv](https://pypi.python.org/pypi/virtualenv) installed)

```abenrob$ virtualenv venv```

dependencies installed with pip:

```abenrob$ venv/bin/pip install -r requirements.txt```

run app locally:

```abenrob$ venv/bin/gunicorn run-api:app```

try it out:

```abenrob$ curl http://localhost:8000/fire/api/v1.0/2013-09-18```


or visit the app deployed to heroku:

http://fire-api.herokuapp.com/fire/api/v1.0/2013-09-18

