from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
productos = []

class Producto(Resource):
    def get(self, valor):
        for p in productos:
            if p == valor:
                return {'Producto buscado': p}

        return {'Resultados': 'Producto no encontrado'}

    def post(self, valor):
        producto = valor
        productos.append(producto)
        return {'Resultados': 'Producto agregado'}

    def delete(self, valor):
        for indice, p, in enumerate(productos):
            if p == valor:
                productos.pop(indice)
                return {'Resultados': 'Producto eliminado'}

class Listar(Resource):
    def get(self):
        return {'Resultados': productos}

api.add_resource(Producto, '/producto/<string:valor>')
api.add_resource(Listar, '/listar')

if __name__ == '__main__':
    app.run(debug=True)