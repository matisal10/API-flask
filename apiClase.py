from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

directorio = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(directorio,'productos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)

Migrate(app, basededatos)

api = Api(app)

class ProductoDB(basededatos.Model):
    nombre = basededatos.Column(basededatos.String(100),primary_key=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def json(self):
        return {'nombre': self.nombre}

class Productos(Resource):
    def get (self, valor):
        producto = ProductoDB.query.filter_by(nombre=valor).first()
        if producto:
            return producto.json()
        return {'resultado':'el producto no existe'}

    def post(self, valor):
        producto = ProductoDB(nombre=valor)
        basededatos.session.add(producto)
        basededatos.session.commit()
        return {'Respuesta':'producto agregado'}

    def delete(self,valor):
        producto = ProductoDB.query.filter_by(nombre=valor).first()
        basededatos.session.delete(producto)
        basededatos.session.commit()
        return {'Respuesta':'producto eliminado'}


class listar(Resource):
    def get(self):
        productos = ProductoDB.query.all()
        lista = [p.json() for p in productos]
        return {'resultado': lista}

api.add_resource(Productos, '/productos/<string:valor>')
api.add_resource(listar, '/listar')

if __name__ == '__main__':
    app.run(debug=True)