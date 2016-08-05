from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport"
     content="width=device-width, initial-scale=1, user-scalable=yes">
  <title>Python Test site</title>
</head>
<body>
<ul>
  <li><a href="/echo">Echo</a></li>
</ul>
</body>
</html>
"""

#@app.route("/echo")
#def echo():
#    return "Echo!"
 
if __name__ == "__main__":
    app.run( port = 5000, host = '0.0.0.0' )

