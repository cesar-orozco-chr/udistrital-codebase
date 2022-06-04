from hashlib import new
# suma/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/suma/<int:a>/<int:b>')
def suma(a, b):
    return str(a+b)

if __name__ == '__main__':
    app.run(host='0.0.0.0')