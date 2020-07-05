from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from functools import wraps
from .db import print_names, delete_user_ui, add_user_ui, edit_user_ui, username_exists, get_user_pw
from .flask_secrets import get_secret_flask_session

app = Flask(__name__)
app.secret_key = get_secret_flask_session()


def check_admin():
    zt = 'username' in session and session['username'] == 'ztauburn'
    dongji = 'username' in session and session['username'] == 'dog'
    return [zt, dongji]


def requires_admin(view):
    @wraps(view)
    def decorated(**kwargs):
        if not check_admin():
            return redirect('/login')
        return view(**kwargs)

    return decorated


@app.route('/debugSession')
def debugSession():
    result = ""
    for key, value in session.items():
        result += key + "->" + str(value) + "<br/>"
    return result


@app.route('/admin/users')
@requires_admin
def users():
    data = print_names()
    return render_template('admin.html', results=data)
    # return render_template(adminPage())


@app.route('/inc')
@requires_admin
def inc():
    if 'value' not in session:
        session['value'] = 0
    session['value'] = session['value'] + 1
    return "<h1>" + str(session['value']) + "</h1>"


@app.route('/invalidLogin')
def invalidLogin():
    return "Invalid"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_pw = get_user_pw(request.form["username"])
        if user_pw is None or user_pw != request.form['password']:
            return redirect('/invalidLogin')
        else:
            session['username'] = request.form["username"]
            return render_template('main.html')
    else:
        return render_template('login.html')


@app.route('/admin')
@requires_admin
def adminPage():
    data = print_names()
    return render_template('admin.html', results=data)


@app.route('/admin/adduser')
@requires_admin
def user_form():
    return render_template('adduser.html')


@app.route('/admin/useradded', methods=['POST'])
@requires_admin
def add_user():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    if username_exists(username):
        return '<h1>USER ' + username + ' ALREADY EXISTS.  <a href="/admin/adduser">TRY A DIFFERENT NAME</a></h1>'
    else:
        add_user_ui(username, password, fullname)
        return '<h1>User ' + username + ' has been added. <a href="/admin"> HOME</a></h1> '


@app.route('/admin/deleteUser/<username>', methods=['POST'])
@requires_admin
def delete_user(username):
    delete_user_ui(username)
    return '<h1>User ' + username + ' has been deleted. <a href="/admin"> HOME</a></h1> '


@app.route('/admin/edituser/<username>')
@requires_admin
def edit_form(username):
    return render_template('edituser.html', username=username)


@app.route('/admin/useredited', methods=['POST'])
@requires_admin
def edit_user():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    edit_user_ui(username, password, fullname)
    return '<h1>User ' + username + ' has been edited. <a href="/admin"> HOME</a></h1> '
