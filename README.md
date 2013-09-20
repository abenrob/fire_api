fire_api
========

simple flask REST api to grab and regurgitate USFS major fires CSV as [geoJSON](http://geojson.org/geojson-spec.html)

get the app:
```abenrob$ git clone https://github.com/abenrob/fire_api.git```

set up the virtual environment (need [virtualenv](https://pypi.python.org/pypi/virtualenv) installed)

```abenrob$ virtualenv venv```

dependencies installed with pip:

```abenrob$ venv/bin/pip install -r requirements.txt```

run app locally:

```abenrob$ venv/bin/gunicorn run-api:app```

try it out:

```abenrob$ curl http://localhost:8000/api/v1.0/2013-09-18```

now rig-up an app! 

--or-- copy the geojson object output from the above step, and paste it in [geojson.io](http://geojson.io/) to [view the geo-goodness](http://geojson.io/#id=gist:abenrob/6aa3119432f222cb4bb6&map=6/42.956/-118.872)!


--or-- visit the app deployed to heroku:

http://fire-api.herokuapp.com/

http://fire-api.herokuapp.com/api/v1.0/2013-09-18

