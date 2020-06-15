from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!",


@app.route('/admin')
def admin():
    return 'admin'


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

@app.route('/mult', methods=['POST'])
def mult():
    x = request.args['x']
    y = request.args['y']
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
