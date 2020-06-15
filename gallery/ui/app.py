
from flask import Flask
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

@app.route('/mult')
def mult():
    x = request.args['x']
    y = request.args['y']
    return 'The product is ' + str[int(x)*int(y)]

@app.route('/calculator')
def calculator():
        return """
        <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Caluclator</title>
	
</head>
<body>
	<form action="/mult" method="GET">
		x: <input value="0" name="x"/><br>
		y: <input value="o" name="y"><br>
		<input type="submit" value="Multiply"/>

	</form>
</body>
</html>
"""