from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Saludo(Resource):
    def get(self):
        return {'saludo': 'Hola mundo'}

api.add_resource(Saludo,'/')

if __name__ == '__main__':
    app.run(debug=True)