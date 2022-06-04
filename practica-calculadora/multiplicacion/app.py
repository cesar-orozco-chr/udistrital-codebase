# multiplicacion/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/multiplicacion/<int:a>/<int:b>')
def multiplicacion(a, b):
    return str(a * b)

if __name__ == '__main__':
    app.run(host='0.0.0.0')