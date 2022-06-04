from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    data = {'001': 'corozcom', '002': 'alejo', '003': 'juan'}
    return render_template('index.html', name=name, users=data)

if __name__ == '__main__':
    app.run(debug=True, port=5004)