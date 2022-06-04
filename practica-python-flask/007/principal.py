from crypt import methods
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = request.files['file']
        result.save(result.filename)
        lista = [ x.split(",") for x in open(result.filename).readlines() ]
        resultados = []
        for x in lista:
            r = sum([int(y) for y in x])
            resultados.append(x + [r])
        return render_template('result.html', datos=resultados)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5004)