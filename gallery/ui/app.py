
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