from crypt import methods
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', data=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5004)