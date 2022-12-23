from flask import Flask
import mysql
import openapi


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/update')
def update():
    return 'null'

if __name__ == '__main__':
    app.run(port=8000)