from flask import Flask, request, jsonify
from flask import Flask ,jsonify ,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow

#Crear la app
back = Flask(__name__)
CORS(back)
                                                      #user:pass@url/nameDB                              
back.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/paquetes_turisticos'
back.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(back) #crea el objeto db de la clase SQLAlchemy
ma=Marshmallow(back) #crea el objeto ma de de la clase Marshmallow

class Destino(db.Model):
# clase Producto hereda de db.Model
# Define los campos de la tabla
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    estadia=db.Column(db.Integer)
    imagen=db.Column(db.String(400))

    def __init__(self,nombre,precio,estadia,imagen):
# crea el constructor de la clase
        self.nombre=nombre
        self.precio=precio
        self.estadia=estadia
        self.imagen=imagen 

with back.app_context():
    db.create_all() # Acá crea todas las tablas  
       
class DestinoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','estadia','imagen')

destino_schema=DestinoSchema()
destinos_schema=DestinoSchema(many=True)


@back.route('/destinos',methods=['GET'])
def get_destinos():
    all_destinos = Destino.query.all()
    return destinos_schema.jsonify(all_destinos)

@back.route('/destinos',methods=['POST'])
def create_destino():
    nombre=request.json['nombre']
    precio=request.json['precio']
    estadia=request.json['estadia']
    imagen=request.json['imagen']

    new_destino = Destino(nombre, precio, estadia, imagen)
    db.session.add(new_destino)
    db.session.commit()

    return destino_schema.jsonify(new_destino)

@back.route('/destinos/<id>',methods=['GET'])
def get_destino(id):
    destino = Destino.query.get(id)

    return destino_schema.jsonify(destino)

@back.route('/destinos/<id>',methods=['DELETE'])
def delete_destinos(id):
    destino=Destino.query.get(id)
    db.session.delete(destino)
    db.session.commit()

    return destino_schema.jsonify(destino)

@back.route('/destinos/<id>',methods=['PUT'])
def update_destinos(id):

    destino=Destino.query.get(id)

    nombre=request.json['nombre']
    precio=request.json['precio']
    estadia=request.json['estadia']
    imagen=request.json['imagen']

    destino.nombre=nombre
    destino.precio=precio
    destino.estadia=estadia
    destino.imagen=imagen

    db.session.commit()

    return destino_schema.jsonify(destino)


#Bloque Principal
if __name__=='__main__':
    back.run(debug=True)