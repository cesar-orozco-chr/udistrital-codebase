from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return "Principal"

@app.route('/<int:pos>')
def position(pos):
    return "Posición " + str(pos)

@app.route('/<float:costo>')
def costo(costo):
    return "Costo : " + str(costo)

if __name__ == '__main__':
    app.run(debug=True, port=5004)