from flask import Flask, render_template, request
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/echo")
def get_echo():
    echo = ''
    txt = request.args.get('txt')
    if txt:
        #echo = "You said: " + request.form['txt']
        echo = "You said: " + txt
    return render_template('echo.html', get_echo = echo)

@app.route("/echo", methods=['POST'])
def post_echo():
    echo = ''
    txt = request.form.get('msg')
    if txt:
        echo = "You submitted: " + txt
    return render_template('echo.html', post_echo = echo)
 
 
if __name__ == "__main__":
    app.run( port = 5000, host = '0.0.0.0' )

# vim: expandtab
