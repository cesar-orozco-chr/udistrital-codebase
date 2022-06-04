from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/<name>")
def name(name):
    return f"Hello {name}!" 

@app.route("/<name>/<lastname>")
def name_lastname(name, lastname):
    return f"Hello {name} {lastname}!" 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004, debug=True)
