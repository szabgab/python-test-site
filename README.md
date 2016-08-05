
Web site to play with various test tools.

Parts of the site are:

* A pure HTML site where the whole thing is generated on the server.
* An application using a JSON API.
* Redirection
* Login with username/password
* Hidden code set in the form.
* Hidden code set in the header.
* Sessions with cookies
* Login with external Single Sign-on service (provided at a separate URL within this site)




Setup for development
----------------------
```
$ virtualenv venv
$ source venv/bin/activate

$ pip install --editable .

$ export FLASK_APP=demo.demo
$ flask run --host 0.0.0.0 --port 5000

$ python -m unittest discover
```

