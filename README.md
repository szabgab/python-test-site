###Status
[![Build Status](https://travis-ci.org/szabgab/python-test-site.png)](https://travis-ci.org/szabgab/python-test-site)

Web site to play with various test tools.

Parts of the site are:

* /     - a pure HTML page where the whole thing is generated on the server.
* /echo - a form that echos back the text one typed in using either a GET or a POST request
* Login with username/password using cookies. Any userN/pwN is a valid login.
* /account - only logged in users can access this page
* /login   - login form and page
* /logout



* An application using a JSON API.
* Redirection
* Hidden code set in the form.
* Hidden code set in the header.
* Login with external Single Sign-on service (provided at a separate URL within this site)




Setup for development
----------------------
```
$ virtualenv venv2 -p /usr/bin/python2
$ source venv2/bin/activate

$ pip install --editable .

$ export FLASK_APP=demo.demo
$ export FLASK_DEBUG=1
$ flask run --host 0.0.0.0 --port 5000

$ python -m unittest discover
```


```
virtualenv venv3 -p /usr/bin/python3
source venv3/bin/activate
pip install --editable .

$ python3 -m unittest discover

```

