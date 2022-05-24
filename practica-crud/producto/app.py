# product
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    deleted = db.Column(db.Boolean, default=0)

    def __init__(self, id, sku, name):
        self.id = id
        self.sku = sku
        self.name = name

    def __str__(self) -> str:
        return "<Product %r>" % self.name


@app.route('/product/add', methods=['POST'])
def add():
    if request.method == 'POST':
        r = json.loads(request.data)
        product = Product(
            r['id'],
            r['sku'],
            r['name']
        )
        db.session.add(product)
        db.session.commit()

        return "Registro guardado", 200


@app.route('/product/list', methods=['GET'])
def list():
    q = Product.query.filter_by(deleted=False).all()
    return jsonify([{'id': p.id, 'sku': p.sku, 'name': p.name} for p in q])


@app.route('/product/edit/<int:id>', methods=['POST'])
def edit(id):
    if request.method == 'POST':
        p = Product.query.get(id)
        d = json.loads(request.data)

        if p is not None:
            p.sku = d['sku']
            p.name = d['name']
            db.session.add(p)
            db.session.commit()

            return "Producto actualizado", 200
        else:

            return "El producto no existe", 402


@app.route('/product/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        p = Product.query.get(id)
        if p is not None:
            p.deleted = 1
            db.session.add(p)
            db.session.commit()
            return "Registro borrado!", 200
        else:
            return "El producto no existe", 402


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')

