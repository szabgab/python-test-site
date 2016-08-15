###Status
[![Build Status](https://travis-ci.org/szabgab/python-test-site.png)](https://travis-ci.org/szabgab/python-test-site)

Web site to play with various test tools.

Parts of the site are:

Respond with HTML:

* /     - a pure HTML page where the whole thing is generated on the server.
* /echo - a form that echos back the text one typed in using either a GET or a POST request
* Login with username/password using cookies. Any userN/pwN is a valid login.
* /account - only logged in users can access this page
* /login   - login form and page
* /logout
* /secure-login  - the GET request returns an HTML with a form with a hidden value
           - when the user clicks on the 'Login' button, the server checks if the given id was returned.

API, Respond with JSON:

* /api/static  - a fixed JSON
* /api/echo    - echo back the given string in a JSON contruct. Both GET and POST are supported.
* /api/account - only logged in users can access this URL



* An application using a JSON API.
* Redirection
* Hidden code set in the form.
* Hidden code set in the header.
* Login with external Single Sign-on service (provided at a separate URL within this site)




Setup for development
----------------------
```
virtualenv venv2 -p /usr/bin/python2
source venv2/bin/activate

pip install --editable .

export FLASK_APP=demo.demo
export FLASK_DEBUG=1
flask run --host 0.0.0.0 --port 5000
```

Alternative running

```
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 demo.demo:app
```


For Python 3 start with:

```
virtualenv venv3 -p /usr/bin/python3
```


Testing
------------

```
python -m unittest discover
```

or

```
python3 -m unittest discover
```

JMeter
-----------
Assuming the server is running on 127.0.0.1:5000 there are a number of JMX files
one can use to test the "application".

In the `jmeter/` directory:

demo_main_page.jmx

demo_login.jmx      using demo_users.csv
demo_mixer.jmx
demo_secure_login.jmx


Selenium on OSX
----------------


```
virtualenv osx2
source osx2/bin/activate
pip install selenium
```

Download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/
Unzip it and put the chromedriver into osx2/bin/

