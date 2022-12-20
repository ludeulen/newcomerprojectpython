from flask import Flask
import consumption
import mysql

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/consumer')
def consumer():
    return mysql.consumer()

if __name__ == '__main__':
    app.run(port=8000)