
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Zum!'

@app.route('/admin')
def admin():
    return 'admin'