from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.route("/")
def home():
	return render_template('index.html')

#@app.route("/echo")
#def echo():
#    return "Echo!"
 
if __name__ == "__main__":
    app.run( port = 5000, host = '0.0.0.0' )

