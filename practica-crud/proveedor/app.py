# provider
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(40), nullable=False)
    deleted = db.Column(db.Boolean, default=0)

    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country

    def __str__(self) -> str:
        return "<Provider %r>" % self.name


@app.route('/provider/add', methods=['POST'])
def add():
    if request.method == 'POST':
        r = json.loads(request.data)
        p = Provider(
            r['id'],
            r['name'],
            r['country']
        )
        db.session.add(p)
        db.session.commit()

        return "Registro guardado", 200


@app.route('/provider/list', methods=['GET'])
def list():
    q = Provider.query.filter_by(deleted=False).all()
    return jsonify([{'id': p.id, 'name': p.name, 'country': p.country} for p in q])


@app.route('/provider/edit/<int:id>', methods=['POST'])
def edit(id):
    if request.method == 'POST':
        p = Provider.query.get(id)
        d = json.loads(request.data)

        if p is not None:
            p.name = d['name']
            p.country = d['country']
            db.session.add(p)
            db.session.commit()

            return "Registro actualizado", 200
        else:

            return "El registro no existe", 402


@app.route('/provider/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        p = Provider.query.get(id)
        if p is not None:
            p.deleted = 1
            db.session.add(p)
            db.session.commit()
            return "Registro borrado!", 200
        else:
            return "El registro no existe", 402


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')

