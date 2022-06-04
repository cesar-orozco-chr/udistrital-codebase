# division/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/division/<int:a>/<int:b>')
def resta(a, b):
    if b > 0:
        return str(a/b)
    else:
        return "No se puede dividir por 0"

if __name__ == '__main__':
    app.run(host='0.0.0.0')