from flask import Flask
from flask import request
from flask import render_template
from db import print_names, delete_user_ui, add_user_ui, edit_user_ui, username_exists

from markupsafe import escape

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return print_names()


# return "hello world!"


@app.route('/admin')
def adminPage():
    data = print_names()
    return render_template('admin.html', results=data)


@app.route('/greet/<name>')
def greet(name):
    return 'Nice to meet you ' + name


# @app.route('/add/<int:x>/<int:y>', methods=['GET'])
# def add(x, y):
#     return 'The sum is ' + str(x + y)
#
@app.route('/calculator/<personsName>')
def calculator(personsName):
    return render_template('form.html', name=personsName)


@app.route('/admin/adduser')
def user_form():
    return render_template('adduser.html')


@app.route('/admin/useradded', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    if username_exists(username):
        return '<h1>USER ALREADY EXISTS.  TRY A DIFFERENT NAME</h1>'
    else:
        add_user_ui(username, password, fullname)
        data = adminPage()
        return data


@app.route('/admin/deleteUser/<username>', methods=['POST'])
def delete_user(username):
    delete_user_ui(username)

    return '<h1>User ' + username + 'deleted. <a href="/admin">HOME</a></h1> '



@app.route('/admin/edituser/<username>')
def edit_form(username):
    return render_template('edituser.html', username=username)


@app.route('/admin/useredited', methods=['POST'])
def edit_user():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    edit_user_ui(username, password, fullname)
    data = adminPage()
    return data


@app.route('/mult', methods=['POST'])
def mult():
    x = request.form['x']
    y = request.form['y']
    return 'The product is ' + str(int(x) * int(y))



