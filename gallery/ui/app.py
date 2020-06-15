
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world!",

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/admin/<name>')
def admin(name):
    return 'Nice to meet you ' + name