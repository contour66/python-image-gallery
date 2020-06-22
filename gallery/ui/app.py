from flask import Flask
from flask import request
from flask import render_template
from db import  print_names, delete_user_ui, add_user_ui, edit_user_ui, username_exists 



app = Flask(__name__)


@app.route('/admin')
def adminPage():
    data = print_names()
    return render_template('admin.html', results=data)


@app.route('/admin/adduser')
def user_form():
    return render_template('adduser.html')


@app.route('/admin/useradded', methods=['POST'])
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
def delete_user(username):
    delete_user_ui(username)
    return '<h1>User ' + username + ' has been deleted. <a href="/admin"> HOME</a></h1> '


@app.route('/admin/edituser/<username>')
def edit_form(username):
    return render_template('edituser.html', username=username)


@app.route('/admin/useredited', methods=['POST'])
def edit_user():
    username = request.form['username']
    password = request.form['password']
    fullname = request.form['fullname']
    edit_user_ui(username, password, fullname)
    return '<h1>User ' + username + ' has been edited. <a href="/admin"> HOME</a></h1> '



