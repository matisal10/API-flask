from flask import Flask, jsonify, request
from productos import products

app = Flask(__name__)

@app.route('/hola', methods=['GET'])
def hola():
    return jsonify({'respuesta':'Mundo!'})

@app.route('/productos')
def productos():
    return jsonify({'productos':products})

@app.route('/productos', methods=['post'])
def addProducts():
    nuevoProducto = {
    'nombre': request.json['nombre'],
    'precio': request.json['precio'],
    'cantidad': request.json['cantidad'],
    }
    products.append(nuevoProducto)
    return jsonify({'productos':products})

@app.route('/productos/<string:nombreProduct>')
def getNombreProducto(nombreProduct):
    productsF =[
        producto for producto in products if producto['nombre'] == nombreProduct.lower()
    ]
    if (len(productsF) > 0):
        return jsonify({'respuesta': productsF})
    return jsonify({'Mensaje': 'producto no encontrado'})

@app.route('/productos/<string:nombreProduct>', methods=['PUT'])
def editProduct(nombreProduct):
    productosF = [
        producto for producto in products if producto['nombre'] == nombreProduct.lower()
    ]
    if (len(productosF) > 0):
        productosF[0]['nombre'] = request.json['nombre']
        productosF[0]['precio'] = request.json['precio']
        productosF[0]['cantidad'] = request.json['cantidad']
        return jsonify({'mensaje':'producto actualizado','productos':productosF})
    return jsonify({'Mensaje': 'producto no actualizado'})

@app.route('/productos/<string:nombreProduct>', methods=['DELETE'])
def deleteProd(nombreProduct):
    productosF = [
        producto for producto in products if producto['nombre'] == nombreProduct.lower()
    ]
    if (len(productosF) > 0):
        products.remove(productosF[0])
        return jsonify({'mensaje':'producto eliminado','productos':products})
    return jsonify({'Mensaje': 'producto no eliminado'})

if __name__ == '__main__':
    app.run(debug=True)