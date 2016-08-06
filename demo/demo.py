from flask import Flask, render_template, request, session
import re

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='development key',
))
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
        echo = "You posted: " + txt
    return render_template('echo.html', post_echo = echo)

@app.route("/account")
def account():
    if 'username' in session:
        return render_template('account.html', 
            username=session['username']
        )
    return render_template('401.html'), 401

@app.route("/login")
def get_login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        m = re.search(r'^user(\d+)$', username)
        if m and password == 'pw' + m.group(1):
            session['username'] = username
            return render_template('login.html', 
                success=True,
                username=session['username']
            )
    return render_template('login.html', 
        error=True
    )

@app.route("/logout")
def logout():
    session.pop('username', 'None')
    return render_template('logout.html')

 
if __name__ == "__main__":
    app.run( port = 5000, host = '0.0.0.0' )

# vim: expandtab
