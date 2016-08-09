from flask import Flask, render_template, request, session, jsonify
import re
import random

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

@app.route("/secure-login")
def get_secure_login():
    username = session.get('username', '')
    if username:
        # TODO remove success
        return render_template('login.html',
            username=username,
            success=success
        )
    
    # TODO also add timeout to the code
    code = str(random.randint(1000, 10000))
    session['code'] = code
    return render_template('secure_login.html',
        code=code
    )

@app.route("/secure-login", methods=['POST'])
def post_secure_login():
    code = request.form.get('code')
    expected_code = session.get('code', '')
    if not expected_code:
        return render_template('secure_login.html', 
            code=expected_code,
            error="No code was expected"
        )
    if not code:
        return render_template('secure_login.html', 
            code=expected_code,
            error="No code received"
        )
    if code != expected_code:
        return render_template('secure_login.html', 
            code=expected_code,
            error="Secret code mismatch. Expected " + expected_code + " Received: " + code
        )

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
    return render_template('secure_login.html', 
        code=expected_code,
        error="Invalid username/pw pair"
    )



@app.route("/login")
def get_login():
    username = session.get('username', '')
    success = False
    if username:
        success = True
    return render_template('login.html',
        # TODO remove success
        username=username,
        success=success
    )

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

@app.route('/api/static')
def api_static():
    return jsonify(text="Hello World")

@app.route('/api/echo')
def api_get_echo():
    msg = request.args.get('msg')
    if msg:
        return jsonify(text=msg)
    else:
        return jsonify(error="Missing msg"), 400

@app.route("/api/echo", methods=['POST'])
def api_post_echo():
    msg = request.form.get('msg')
    if msg:
        return jsonify(text=msg)
    else:
        return jsonify(error="Missing msg"), 400

@app.route('/api/account')
def api_account():
    if 'username' in session:
        return jsonify(username=session['username'])
    return jsonify(error='Not logged in'), 401

 
if __name__ == "__main__":
    app.run( port = 5000, host = '0.0.0.0' )

# vim: expandtab
