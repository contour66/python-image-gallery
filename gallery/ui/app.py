from flask import Flask
from flask import request
from flask import render_template
from db import print_names, delete_user_ui

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


@app.route('/admin/deleteUser,<name>', methods=['POST'])
def delete():
    name = request.form['name']
    return delete_user_ui(str(name))


@app.route('/mult', methods=['POST'])
def mult():
    x = request.form['x']
    y = request.form['y']
    return 'The product is ' + str(int(x) * int(y))

# @app.route('/calculator')
# def calculator():
#     return """
# <!DOCTYPE html>
# <html>
# <head>
# 	<meta charset="utf-8">
# 	<title>Caluclator</title>
#
# </head>
# <body>
# 	<form action="/mult" method="GET">
# 		x: <input  name="x" value="0"/><br/>
# 		y: <input name="y" value="0" /><br/>
# 		<input type="submit" value="Multiply"/>
# 	</form>
# </body>
# </html>
# """

# List users, as links, without password information.
# Each user should have a "delete" link next to them which deletes the selected user after a confirmation.
# Clicking on a "user" links should bring you to a "modify user" page which lets you either edit the user.
# The admin page should also have a link/button to create users.
