from unicodedata import name
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "hola admin"

@app.route('/user/<name>')
def user(name):
    return "hola " + name

@app.route('/index/<user>')
def index(user):
    if user == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('user', name=user))

if __name__ == '__main__':
    app.run(debug=True, port=5004)